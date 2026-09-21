from pathlib import Path
import json

from langchain_chroma import Chroma

from local_embeddings import LocalEmbeddingFunction


# --------------------------------------------------
# 1. Project paths
# --------------------------------------------------

project_root = Path(__file__).parent.parent

chunks_path = (
    project_root
    / "data"
    / "processed"
    / "chunks.json"
)

vector_db_path = (
    project_root
    / "data"
    / "vector_db"
)


# --------------------------------------------------
# 2. Load chunks
# --------------------------------------------------

with open(chunks_path, "r", encoding="utf-8") as file:
    chunks = json.load(file)

print(f"Loaded chunks: {len(chunks)}")


# --------------------------------------------------
# 3. Prepare data
# --------------------------------------------------

texts = []
metadatas = []
ids = []

for chunk in chunks:

    texts.append(chunk["text"])

    metadatas.append(
        {
            "page": chunk["page"],
            "chunk_number": chunk["chunk_number"],
        }
    )

    ids.append(str(chunk["chunk_id"]))


# --------------------------------------------------
# 4. Load local embedding model
# --------------------------------------------------

embeddings = LocalEmbeddingFunction()


# --------------------------------------------------
# 5. Create Chroma vector store
# --------------------------------------------------

vector_store = Chroma(
    collection_name="farmer_knowledge",
    embedding_function=embeddings,
    persist_directory=str(vector_db_path),
)


# --------------------------------------------------
# 6. Add chunks
# --------------------------------------------------

print("Creating embeddings and storing chunks...")

vector_store.add_texts(
    texts=texts,
    metadatas=metadatas,
    ids=ids,
)


# --------------------------------------------------
# 7. Verify database
# --------------------------------------------------

stored_count = vector_store._collection.count()

print("\nVector database created successfully.")
print(f"Chunks stored: {stored_count}")
print(f"Database location: {vector_db_path}")