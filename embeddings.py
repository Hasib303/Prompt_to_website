import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle


def load_embedding_model(model_name):
    print(f"Loading embedding model: {model_name}")
    model = SentenceTransformer(model_name)
    return model


def create_text_from_row(row):
    text = f"{row['name']} - {row['category']}. {row['description']}. Use cases: {row['use_cases']}"
    return text


def create_embeddings_from_csv(csv_path, model):
    print(f"Loading components from {csv_path}")
    df = pd.read_csv(csv_path)
    
    texts = []
    metadata = []
    
    for _, row in df.iterrows():
        text = create_text_from_row(row)
        texts.append(text)
        
        metadata_item = {
            'component_id': row['component_id'],
            'name': row['name'],
            'category': row['category'],
            'description': row['description'],
            'code_snippet': row['code_snippet'],
            'use_cases': row['use_cases']
        }
        metadata.append(metadata_item)
    
    print(f"Creating embeddings for {len(texts)} components...")
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    
    return embeddings, metadata


def save_metadata(metadata, path):
    with open(path, 'wb') as f:
        pickle.dump(metadata, f)
    print(f"Saved metadata to {path}")


def load_metadata(path):
    with open(path, 'rb') as f:
        metadata = pickle.load(f)
    return metadata