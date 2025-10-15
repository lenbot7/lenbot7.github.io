import requests
import yaml
import os
import argparse

def make_slug(title):
    return (
        "".join(c if c.isalnum() or c in "-_" else "-" for c in title.lower())
        .replace("--", "-")
        .strip("-")
    )

def parse_pub_date(pub_date):
    year = pub_date.get("year", {}).get("value", "2000") if pub_date else "2000"
    month = pub_date.get("month", {}).get("value", "01") if pub_date and pub_date.get("month") else "01"
    day = pub_date.get("day", {}).get("value", "01") if pub_date and pub_date.get("day") else "01"
    if month == "00" or not month.isdigit() or int(month) < 1 or int(month) > 12:
        month = "01"
    if not day or not day.isdigit() or int(day) < 1 or int(day) > 31:
        day = "01"
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

def extract_ids(external_ids):
    # Returns dict of ids (doi, pmid, pmc, etc)
    ids = {}
    for extid in external_ids.get("external-id", []):
        id_type = extid.get("external-id-type", "").lower()
        id_value = extid.get("external-id-value", "")
        id_url = extid.get("external-id-url", "")
        if id_type and id_value:
            ids[id_type] = {"value": id_value, "url": id_url}
    return ids

def write_post(work, output_dir):
    title = work.get("title", {}).get("title", {}).get("value", "Untitled Publication")
    pub_date = parse_pub_date(work.get("publication-date"))
    slug = make_slug(title)
    filename = f"{pub_date}-{slug}.md"

    journal = work.get("journal-title", "")
    pub_type = work.get("type", "")
    ids = extract_ids(work.get("external-ids", {}))
    doi = ids.get("doi", {}).get("value", "")
    doi_url = ids.get("doi", {}).get("url", "")
    pmid = ids.get("pmid", {}).get("value", "")
    pmc = ids.get("pmc", {}).get("value", "")
    url = work.get("url", "")
    if not url and doi_url:
        url = doi_url

    front_matter = {
        "title": title,
        "date": pub_date,
        "journal": journal,
        "type": pub_type,
        "doi": doi,
        "pmid": pmid,
        "pmc": pmc,
        "url": url,
        "tags": ["publication"],
    }

    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml.dump(front_matter, sort_keys=False, allow_unicode=True))
        f.write("---\n\n")
        f.write(f"*Published in*: {journal}\n\n")
        if doi_url:
            f.write(f"[DOI link]({doi_url})\n\n")
        if url and url != doi_url:
            f.write(f"[Read online]({url})\n\n")
        f.write("\n")

def main():
    parser = argparse.ArgumentParser(description="Fetch ORCID works and create Jekyll posts, meow~ :3")
    parser.add_argument("--orcid-id", required=True, help="The ORCID iD of the author, nya!")
    parser.add_argument("--output-dir", default="_posts", help="Directory to write Jekyll posts, nya~")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    url = f"https://pub.orcid.org/v3.0/{args.orcid_id}/works"
    headers = {"Accept": "application/json"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()

    count = 0
    for group in data.get("group", []):
        for work in group.get("work-summary", []):
            write_post(work, args.output_dir)
            count += 1
    print(f"All posts written to {args.output_dir}, nya~ ({count} publications)")

if __name__ == "__main__":
    main()
