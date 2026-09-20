from pathlib import Path
import json

from langchain_text_splitters import RecursiveCharacterTextSplitter


# --------------------------------------------------
# 1. Load cleaned pages
# --------------------------------------------------

project_root = Path(__file__).parent.parent

input_path = (
    project_root
    / "data"
    / "processed"
    / "cleaned_pages.json"
)

with open(input_path, "r", encoding="utf-8") as file:
    pages = json.load(file)

print(f"Loaded cleaned pages: {len(pages)}")


# --------------------------------------------------
# 2. Create text splitter
# --------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)


# --------------------------------------------------
# 3. Create chunks
# --------------------------------------------------

chunks = []

for page in pages:

    page_chunks = text_splitter.split_text(page["text"])

    for chunk_number, text in enumerate(page_chunks):

        chunks.append(
            {
                "chunk_id": len(chunks),
                "page": page["page"],
                "chunk_number": chunk_number,
                "text": text,
            }
        )


# --------------------------------------------------
# 4. Statistics
# --------------------------------------------------

chunk_lengths = [
    len(chunk["text"])
    for chunk in chunks
]

print(f"Total chunks: {len(chunks)}")
print(
    f"Average chunk size: "
    f"{sum(chunk_lengths) / len(chunk_lengths):.0f} characters"
)
print(f"Shortest chunk: {min(chunk_lengths)} characters")
print(f"Longest chunk: {max(chunk_lengths)} characters")


# --------------------------------------------------
# 5. Save
# --------------------------------------------------

output_path = (
    project_root
    / "data"
    / "processed"
    / "chunks.json"
)

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(
        chunks,
        file,
        ensure_ascii=False,
        indent=2,
    )

print(f"Saved chunks to: {output_path}")


# --------------------------------------------------
# 6. Inspect examples
# --------------------------------------------------

print("\n--- AGRICULTURAL CONTENT CHUNKS ---")

shown = 0

for chunk in chunks:

    if chunk["page"] >= 16:

        print("\n" + "=" * 70)
        print(
            f"CHUNK {chunk['chunk_id']} "
            f"| PDF PAGE {chunk['page']}"
        )
        print("=" * 70)

        print(chunk["text"])

        shown += 1

        if shown == 5:
            break