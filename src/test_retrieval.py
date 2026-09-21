from pathlib import Path

from langchain_chroma import Chroma

from local_embeddings import LocalEmbeddingFunction


# --------------------------------------------------
# 1. Paths
# --------------------------------------------------

project_root = Path(__file__).parent.parent

vector_db_path = (
    project_root
    / "data"
    / "vector_db"
)


# --------------------------------------------------
# 2. Load embedding model
# --------------------------------------------------

embeddings = LocalEmbeddingFunction()


# --------------------------------------------------
# 3. Load existing vector database
# --------------------------------------------------

vector_store = Chroma(
    collection_name="farmer_knowledge",
    embedding_function=embeddings,
    persist_directory=str(vector_db_path),
)


# --------------------------------------------------
# 4. Ask a question
# --------------------------------------------------
query = (
    "To establish a new coconut orchard in the Andaman "
    "and Nicobar Islands, what planting recommendations "
    "are given for healthy disease-free seedlings?"
)

print(f"\nQUERY:\n{query}")


# --------------------------------------------------
# 5. Retrieve similar chunks
# --------------------------------------------------

results = vector_store.similarity_search_with_score(
    query,
    k=5,
)


# --------------------------------------------------
# 6. Display results
# --------------------------------------------------

print("\n" + "=" * 80)
print("TOP RETRIEVED CHUNKS")
print("=" * 80)

for rank, (document, score) in enumerate(results, start=1):

    print("\n" + "-" * 80)
    print(f"RESULT {rank}")
    print(f"Similarity score: {score}")
    print(f"PDF page: {document.metadata.get('page')}")
    print(
        f"Chunk number: "
        f"{document.metadata.get('chunk_number')}"
    )
    print("-" * 80)

    print(document.page_content)