from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


# Locate documents
documents_folder = Path(__file__).parent.parent / "data" / "documents"
pdf_files = list(documents_folder.glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError("No PDF found in data/documents/")

pdf_path = pdf_files[0]

# Load PDF
loader = PyPDFLoader(str(pdf_path))
documents = loader.load()

print(f"Total pages: {len(documents)}")

# Basic statistics
text_lengths = [len(doc.page_content.strip()) for doc in documents]

print(f"Shortest page: {min(text_lengths)} characters")
print(f"Longest page: {max(text_lengths)} characters")
print(f"Average page: {sum(text_lengths) / len(text_lengths):.0f} characters")

# Empty / nearly empty pages
threshold = 100

short_pages = [
    (i + 1, length)
    for i, length in enumerate(text_lengths)
    if length < threshold
]

print(f"\nPages with fewer than {threshold} characters: {len(short_pages)}")

print("\nFirst 20 short pages:")

for page_number, length in short_pages[:20]:
    print(f"Page {page_number}: {length} characters")