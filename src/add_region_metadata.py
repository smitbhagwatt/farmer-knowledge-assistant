from pathlib import Path
import json


project_root = Path(__file__).parent.parent

input_path = (
    project_root
    / "data"
    / "processed"
    / "cleaned_pages.json"
)

output_path = (
    project_root
    / "data"
    / "processed"
    / "pages_with_regions.json"
)


# Actual regional section starts identified from the document
region_starts = {
    16: "Andaman & Nicobar Islands",
    20: "Andhra Pradesh",
    34: "Arunachal Pradesh",
    40: "Assam",
    48: "Bihar",
    54: "Chhattisgarh",
    62: "Goa",
    66: "Gujarat",
    76: "Haryana & Delhi",
    84: "Himachal Pradesh",
    102: "Punjab",
    120: "Jharkhand",
    126: "Karnataka",
    136: "Kerala",
    140: "Ladakh",
    146: "Lakshadweep",
    149: "Madhya Pradesh",
    154: "Maharashtra",
    178: "Manipur",
    184: "Meghalaya",
    188: "Mizoram",
    194: "Nagaland",
    202: "Odisha",
    224: "Rajasthan",
    248: "Sikkim",
    254: "Tamil Nadu",
    258: "Telangana",
    266: "Tripura",
    268: "Uttar Pradesh",
    280: "Uttarakhand",
    296: "West Bengal",
}


with open(input_path, "r", encoding="utf-8") as file:
    pages = json.load(file)


# Sort section starts by page number
sorted_starts = sorted(region_starts.items())


current_region = None
pages_with_regions = []


for page in pages:

    page_number = page["page"]

    # Check whether this page starts a new region
    if page_number in region_starts:
        current_region = region_starts[page_number]

    pages_with_regions.append(
        {
            "page": page_number,
            "region": current_region,
            "text": page["text"],
        }
    )


with open(output_path, "w", encoding="utf-8") as file:
    json.dump(
        pages_with_regions,
        file,
        ensure_ascii=False,
        indent=2,
    )


print(f"Processed pages: {len(pages_with_regions)}")
print(f"Saved to: {output_path}")

print("\nREGION ASSIGNMENTS")
print("=" * 70)

for page in pages_with_regions:
    print(
        f"PDF page {page['page']:>3}"
        f" → {page['region']}"
    )