import config
import scraper
import embeddings
import vector_store
import generator
from pathlib import Path


def setup_knowledge_base():
    print("="*60)
    print("STEP 1: Setting up Knowledge Base")
    print("="*60)
    
    # Check if data already exists
    if config.COMPONENTS_CSV.exists():
        print(f"Components CSV already exists at {config.COMPONENTS_CSV}")
    else:
        print("Scraping and creating component database...")
        scraper.scrape_and_save(config.COMPONENTS_CSV)
    
    print("\n" + "="*60)
    print("STEP 2: Creating Embeddings")
    print("="*60)
    
    # Load embedding model
    model = embeddings.load_embedding_model(config.EMBEDDING_MODEL)
    
    # Create embeddings
    emb_vectors, metadata = embeddings.create_embeddings_from_csv(
        config.COMPONENTS_CSV, 
        model
    )
    
    print("\n" + "="*60)
    print("STEP 3: Building Vector Database")
    print("="*60)
    
    # Build and save FAISS index
    vector_store.build_vector_database(
        emb_vectors,
        metadata,
        config.FAISS_INDEX_PATH,
        config.METADATA_PATH
    )
    
    print("\n✅ Knowledge base setup complete!\n")


def generate_website(user_query):
    print("="*60)
    print("STEP 1: Loading Vector Database")
    print("="*60)
    
    index = vector_store.load_index(config.FAISS_INDEX_PATH)
    metadata = embeddings.load_metadata(config.METADATA_PATH)
    
    print("\n" + "="*60)
    print("STEP 2: Loading Embedding Model")
    print("="*60)
    
    model = embeddings.load_embedding_model(config.EMBEDDING_MODEL)
    
    print("\n" + "="*60)
    print("STEP 3: Retrieving Relevant Components")
    print("="*60)
    
    results = vector_store.search_similar_components(
        user_query,
        model,
        index,
        metadata,
        top_k=config.TOP_K_RESULTS
    )
    
    print(f"\nFound {len(results)} relevant components:")
    for i, result in enumerate(results, 1):
        print(f"  {i}. {result['name']} (Score: {result['similarity_score']:.3f})")
    
    print("\n" + "="*60)
    print("STEP 4: Generating Website Code")
    print("="*60)
    
    # Generate website
    website_code = generator.generate_website_code(user_query, results)
    
    # Save generated website
    output_dir = config.BASE_DIR / 'generated'
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / 'website.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(website_code)
    
    print(f"\n✅ Website generated successfully!")
    print(f"📄 Saved to: {output_file}")
    print(f"🌐 Open the file in your browser to view the website\n")
    
    return website_code, output_file


def main():
    print("\n" + "="*60)
    print("     RAG WEBSITE GENERATOR")
    print("="*60 + "\n")
    
    if not config.FAISS_INDEX_PATH.exists():
        print("Knowledge base not found. Setting up...")
        setup_knowledge_base()
    else:
        print("Knowledge base found. Skipping setup.\n")
    
    while True:
        print("\n" + "-"*60)
        user_query = input("\nEnter your website request (or 'quit' to exit):\n> ").strip()
        
        if user_query.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!\n")
            break
        
        if not user_query:
            print("Please enter a valid request.")
            continue
        
        website_code, output_file = generate_website(user_query)
        
        print("\n" + "-"*60)
        print("Want to generate another website? Enter a new request or 'quit'")


if __name__ == "__main__":
    main()