from pathlib import Path
import json
import re


# --------------------------------------------------
# 1. Paths
# --------------------------------------------------

project_root = Path(__file__).parent.parent

input_path = (
    project_root
    / "data"
    / "processed"
    / "cleaned_pages.json"
)


# --------------------------------------------------
# 2. Load cleaned pages
# --------------------------------------------------

with open(input_path, "r", encoding="utf-8") as file:
    pages = json.load(file)


# --------------------------------------------------
# 3. Known regions
# --------------------------------------------------

regions = [
    "Andaman & Nicobar Islands",
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana & Delhi",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Ladakh",
    "Lakshadweep",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
]


# --------------------------------------------------
# 4. Find likely region headings
# --------------------------------------------------

print("LIKELY REGION HEADINGS")
print("=" * 70)

detections = []

for page in pages:

    text = page["text"].strip()

    # Region headings should normally appear near
    # the beginning of a regional section.
    beginning = text[:300]

    for region in regions:

        pattern = rf"(?<!\w){re.escape(region)}(?!\w)"

        if re.search(pattern, beginning, re.IGNORECASE):

            detections.append(
                {
                    "page": page["page"],
                    "region": region,
                    "preview": beginning[:180].replace("\n", " "),
                }
            )


# --------------------------------------------------
# 5. Display results
# --------------------------------------------------

for detection in detections:

    print(
        f"\nPDF page {detection['page']:>3}"
        f" → {detection['region']}"
    )

    print(f"  {detection['preview']}")


print("\n" + "=" * 70)
print(f"Total likely headings: {len(detections)}")