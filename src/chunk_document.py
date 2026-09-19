from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# 1. Find the documents folder
documents_folder = Path(__file__).parent.parent / "data" / "documents"

# 2. Find PDF files
pdf_files = list(documents_folder.glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError("No PDF found in data/documents/")

# 3. Select the first PDF
pdf_path = pdf_files[0]

print(f"Loading: {pdf_path.name}")

# 4. Load the PDF
loader = PyPDFLoader(str(pdf_path))
documents = loader.load()

print(f"Pages loaded: {len(documents)}")

# 5. Create the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

# 6. Split the documents into chunks
chunks = text_splitter.split_documents(documents)

print(f"Chunks created: {len(chunks)}")

# 7. Inspect the first 10 pages
for i, page in enumerate(documents[10:20], start=11):

    print("\n" + "=" * 60)
    print(f"PAGE {i + 1}")
    print("=" * 60)

    print("\nTEXT:")
    print(page.page_content[:500])

    print("\nMETADATA:")
    print(page.metadata)