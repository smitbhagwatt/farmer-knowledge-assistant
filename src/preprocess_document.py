from pathlib import Path
import json
import re

from langchain_community.document_loaders import PyPDFLoader


# --------------------------------------------------
# 1. Locate PDF
# --------------------------------------------------

documents_folder = Path(__file__).parent.parent / "data" / "documents"
pdf_path = next(documents_folder.glob("*.pdf"))

print(f"Loading: {pdf_path.name}")


# --------------------------------------------------
# 2. Load PDF
# --------------------------------------------------

loader = PyPDFLoader(str(pdf_path))
documents = loader.load()

print(f"Raw pages: {len(documents)}")


# --------------------------------------------------
# 3. Clean text
# --------------------------------------------------

def clean_text(text: str) -> str:
    """
    Perform conservative text cleaning.

    We deliberately avoid aggressive corrections because
    changing source content can alter its meaning.
    """

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove repeated spaces/tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# --------------------------------------------------
# 4. Remove exact duplicate pages
# --------------------------------------------------

unique_documents = []
seen_text = set()

for document in documents:

    original_page = document.metadata.get("page", 0) + 1

    raw_text = document.page_content.strip()

    # Skip empty pages
    if not raw_text:
        continue

    cleaned_text = clean_text(raw_text)

    # Skip exact duplicates
    if cleaned_text in seen_text:
        continue

    seen_text.add(cleaned_text)

    unique_documents.append(
        {
            "page": original_page,
            "text": cleaned_text,
        }
    )


# --------------------------------------------------
# 5. Save cleaned pages
# --------------------------------------------------

output_folder = Path(__file__).parent.parent / "data" / "processed"
output_folder.mkdir(parents=True, exist_ok=True)

output_path = output_folder / "cleaned_pages.json"

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(
        unique_documents,
        file,
        ensure_ascii=False,
        indent=2,
    )


# --------------------------------------------------
# 6. Report
# --------------------------------------------------

print(f"\nUnique pages: {len(unique_documents)}")
print(f"Removed pages: {len(documents) - len(unique_documents)}")
print(f"Saved to: {output_path}")


# --------------------------------------------------
# 7. Inspect samples
# --------------------------------------------------

print("\n--- SAMPLE CLEANED PAGES ---")

for document in unique_documents[:5]:

    print("\n" + "=" * 60)
    print(f"ORIGINAL PDF PAGE: {document['page']}")
    print("=" * 60)

    print(document["text"][:500])