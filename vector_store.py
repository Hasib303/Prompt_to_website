import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer


def create_faiss_index(dimension):
    index = faiss.IndexFlatL2(dimension)
    return index


def add_vectors_to_index(index, embeddings):
    embeddings_float32 = embeddings.astype('float32')
    index.add(embeddings_float32)
    print(f"Added {len(embeddings)} vectors to FAISS index")
    return index


def save_index(index, index_path):
    faiss.write_index(index, str(index_path))
    print(f"Saved FAISS index to {index_path}")


def load_index(index_path):
    index = faiss.read_index(str(index_path))
    print(f"Loaded FAISS index from {index_path}")
    return index


def search_similar_components(query_text, model, index, metadata, top_k=5):
    query_embedding = model.encode([query_text], convert_to_numpy=True)[0]
    query_embedding = query_embedding.astype('float32').reshape(1, -1)
    
    distances, indices = index.search(query_embedding, top_k)
    
    results = []
    for idx, distance in zip(indices[0], distances[0]):
        if idx < len(metadata):
            result = metadata[idx].copy()
            result['similarity_score'] = float(1 / (1 + distance))
            results.append(result)
    
    return results


def build_vector_database(embeddings, metadata, index_path, metadata_path):
    dimension = embeddings.shape[1]
    index = create_faiss_index(dimension)
    index = add_vectors_to_index(index, embeddings)
    save_index(index, index_path)
    
    with open(metadata_path, 'wb') as f:
        pickle.dump(metadata, f)
    
    print("Vector database built successfully!")
    return index