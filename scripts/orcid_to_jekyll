import requests
import yaml
import os
import argparse

def fetch_orcid_works(orcid_id):
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
    headers = {"Accept": "application/json"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

def make_slug(title):
    return (
        "".join(c if c.isalnum() or c in "-_" else "-" for c in title.lower())
        .replace("--", "-")
        .strip("-")
    )

def write_post(work, output_dir):
    title = work.get("title", {}).get("title", {}).get("value", "Untitled Publication")
    pub_date = "2000-01-01"
    if "publication-date" in work and "year" in work["publication-date"]:
        year = work["publication-date"].get("year", {}).get("value", "2000")
        month = work["publication-date"].get("month", {}).get("value", "01")
        day = work["publication-date"].get("day", {}).get("value", "01")
        pub_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    slug = make_slug(title)
    filename = f"{pub_date}-{slug}.md"
    authors = [c.get("credit-name", {}).get("value", "") for c in work.get("contributors", {}).get("contributor", [])]
    doi = ""
    for ext_id in work.get("external-ids", {}).get("external-id", []):
        if ext_id.get("external-id-type") == "doi":
            doi = ext_id.get("external-id-value", "")
    abstract = work.get("short-description", "")

    front_matter = {
        "title": title,
        "date": pub_date,
        "authors": authors,
        "doi": doi,
        "tags": ["publication"],
    }
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml.dump(front_matter, sort_keys=False))
        f.write("---\n\n")
        f.write(f"{abstract}\n")

def main():
    parser = argparse.ArgumentParser(description="Fetch ORCID works and create Jekyll posts, meow~")
    parser.add_argument("--orcid-id", required=True, help="The ORCID iD of the author, nya!")
    parser.add_argument("--output-dir", default="_posts", help="Directory to write Jekyll posts, nya~")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    data = fetch_orcid_works(args.orcid_id)
    works = data.get("group", [])
    print(f"Fetched {len(works)} works, mrow~")
    for group in works:
        if "work-summary" in group and group["work-summary"]:
            for work in group["work-summary"]:
                write_post(work, args.output_dir)
    print("All posts written to", args.output_dir, "nya~!")

if __name__ == "__main__":
    main()
