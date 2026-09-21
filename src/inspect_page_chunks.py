from pathlib import Path
import json


project_root = Path(__file__).parent.parent

chunks_path = (
    project_root
    / "data"
    / "processed"
    / "chunks.json"
)

with open(chunks_path, "r", encoding="utf-8") as file:
    chunks = json.load(file)


target_page = 18

page_chunks = [
    chunk
    for chunk in chunks
    if chunk["page"] == target_page
]


print(f"PDF page: {target_page}")
print(f"Number of chunks: {len(page_chunks)}")


for chunk in page_chunks:

    print("\n" + "=" * 80)

    print(
        f"CHUNK ID: {chunk['chunk_id']} | "
        f"CHUNK NUMBER: {chunk['chunk_number']}"
    )

    print("=" * 80)

    print(chunk["text"])