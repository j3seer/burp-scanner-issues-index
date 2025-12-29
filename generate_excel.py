import json
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup

ISSUES_DIR = Path("Issues")   # directory containing *.json files
OUTPUT_FILE = "burp_issues.xlsx"


def html_to_text(html):
    """Remove ALL HTML and return clean, readable text."""
    if not html:
        return ""

    soup = BeautifulSoup(html, "lxml")

    # Convert list items into bullet points
    for li in soup.find_all("li"):
        li.insert_before("• ")
        li.append("\n")

    text = soup.get_text(separator="\n")

    # Normalize whitespace / newlines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


rows = []

for json_file in ISSUES_DIR.glob("*.json"):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    name = data.get("name")

    description = html_to_text(data.get("description"))
    remediation = html_to_text(data.get("remediation"))

    references = []
    cwe_capec_ids = []

    # Normal references
    for ref in data.get("references", []):
        url = ref.get("url")
        if url:
            references.append(url)

    # CWE / CAPEC handling
    for vc in data.get("vulnerabilityClassifications", []):
        title = vc.get("title", "")
        url = vc.get("url")

        if title.startswith("CWE-") or title.startswith("CAPEC-"):
            identifier = title.split(":")[0]
            cwe_capec_ids.append(identifier)

            if url:
                references.append(url)

    rows.append({
        "name": name,
        "description": description,
        "remediation": remediation,
        "references": "\n".join(sorted(set(references))),
        "CWE/CAPEC": ", ".join(sorted(set(cwe_capec_ids))),
    })

df = pd.DataFrame(rows)
df.to_excel(OUTPUT_FILE, index=False)

print(f"[+] Saved {len(rows)} issues to {OUTPUT_FILE}")
