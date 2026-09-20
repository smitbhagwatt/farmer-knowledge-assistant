from pathlib import Path
import json


# --------------------------------------------------
# 1. Locate processed dataset
# --------------------------------------------------

project_root = Path(__file__).parent.parent

input_path = project_root / "data" / "processed" / "cleaned_pages.json"

if not input_path.exists():
    raise FileNotFoundError(
        f"Processed file not found: {input_path}"
    )


# --------------------------------------------------
# 2. Load JSON
# --------------------------------------------------

with open(input_path, "r", encoding="utf-8") as file:
    pages = json.load(file)


# --------------------------------------------------
# 3. Basic statistics
# --------------------------------------------------

print(f"Total cleaned pages: {len(pages)}")

text_lengths = [
    len(page["text"])
    for page in pages
]

print(f"Shortest page: {min(text_lengths)} characters")
print(f"Longest page: {max(text_lengths)} characters")
print(f"Average page: {sum(text_lengths) / len(text_lengths):.0f} characters")


# --------------------------------------------------
# 4. Inspect pages around the first state section
# --------------------------------------------------

print("\n--- SAMPLE: PAGES 16-30 IN ORIGINAL PDF ---")

for page in pages:

    if 16 <= page["page"] <= 30:

        print("\n" + "=" * 70)
        print(f"PDF PAGE: {page['page']}")
        print("=" * 70)

        print(page["text"][:1000])