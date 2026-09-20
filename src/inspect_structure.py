from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


documents_folder = Path(__file__).parent.parent / "data" / "documents"
pdf_path = next(documents_folder.glob("*.pdf"))

loader = PyPDFLoader(str(pdf_path))
documents = loader.load()

print(f"Total pages: {len(documents)}")

seen = {}
duplicate_pages = []

for page_number, document in enumerate(documents, start=1):

    text = document.page_content.strip()

    if not text:
        continue

    if text in seen:
        duplicate_pages.append(
            (page_number, seen[text])
        )
    else:
        seen[text] = page_number


print(f"\nTotal duplicate pages: {len(duplicate_pages)}")

print("\nFirst 30 duplicates:")

for duplicate_page, original_page in duplicate_pages[:30]:
    print(
        f"Page {duplicate_page} == Page {original_page}"
    )