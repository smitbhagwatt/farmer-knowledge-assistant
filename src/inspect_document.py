from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

# Finding the PDF inside the documents folder
documents_folder = Path(__file__).parent.parent / "data" / "documents"

pdf_files = list(documents_folder.glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError("No PDF found in data/documents/")

pdf_path = pdf_files[0]

print(f"Loading: {pdf_path.name}")

# Load the PDF
loader = PyPDFLoader(str(pdf_path))
documents = loader.load()

print(f"\nNumber of pages loaded: {len(documents)}")

# Inspect the first page
first_page = documents[0]

print("\n--- FIRST PAGE TEXT ---")
print(first_page.page_content[:2000])

print("\n--- METADATA ---")
print(first_page.metadata)