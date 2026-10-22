#!/usr/bin/env python3
"""
build_dataset.py
Extracts and structures Lethal Autonomous Weapons Systems (LAWS) and military AI
dossiers from aviperera.com into open machine-readable CSV and JSON datasets.
"""

import os
import sys
import json
import csv
import html
import re
import urllib.request
from datetime import datetime, timezone

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

WP_API = "https://aviperera.com/wp-json/wp/v2/posts?per_page=100&_fields=id,slug,link,title,content,date_gmt,categories,tags"
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

SYSTEM_TYPES = {
    "Loitering Munition": ["switchblade", "lancet", "kyb", "hero", "harpy", "skystriker", "kamikaze"],
    "Uncrewed Aerial System (UAS)": ["v-bat", "reaper", "drone", "uav", "okhotnik", "ghost bat", "lanius", "kargu"],
    "Uncrewed Ground Vehicle (UGV)": ["vision 60", "mule", "arcv", "unitree", "sharp claw", "arion-smet", "ugv"],
    "Combat Humanoid": ["humanoid", "fuxi", "skybot", "fedor", "alex ballistic", "nudt"],
    "Targeting & Decision AI": ["maven", "gotham", "lavender", "hivemind", "smash", "predpol", "clearview"]
}

def clean_text(raw_html: str) -> str:
    clean = re.sub(r"<[^>]+>", " ", raw_html)
    return html.unescape(clean).strip()

def detect_system_type(title: str, text: str) -> str:
    combined = (title + " " + text[:500]).lower()
    for category, keywords in SYSTEM_TYPES.items():
        if any(k in combined for k in keywords):
            return category
    return "Military AI / Policy Framework"

def extract_field(pattern: str, text: str, default: str = "Unspecified") -> str:
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        val = match.group(1).strip()
        # Clean markdown or trailing punctuation
        val = re.sub(r"[\*\(\)\[\]]", "", val).strip()
        return val[:120]
    return default

def fetch_and_build() -> list:
    os.makedirs(DATA_DIR, exist_ok=True)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; LAWSOpenDatasetBot/1.0; +https://aviperera.com)"}
    
    print("[*] Fetching research dossiers from aviperera.com...")
    try:
        req = urllib.request.Request(WP_API, headers=headers)
        with urllib.request.urlopen(req, timeout=25) as resp:
            posts = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"[!] Failed to fetch posts from WordPress API: {e}")
        return []

    records = []
    for p in posts:
        title = html.unescape(p.get("title", {}).get("rendered", "")).strip()
        link = p.get("link", "").strip()
        date_gmt = p.get("date_gmt", "").split("T")[0] if p.get("date_gmt") else ""
        raw_content = p.get("content", {}).get("rendered", "")
        clean_content = clean_text(raw_content)

        # Extract structured dimensions
        manufacturer = extract_field(r"Manufacturer[:\*\s]+([^\n\.<]+)", clean_content, "See Dossier")
        country = extract_field(r"Country of origin[:\*\s]+([^\n\.<]+)", clean_content, "International")
        sys_type = detect_system_type(title, clean_content)
        
        # Determine autonomy level or meaningful human control evaluation
        autonomy_note = "Evaluated under Meaningful Human Control (MHC) & IHL"
        if "autonomous" in clean_content.lower():
            autonomy_note = "Autonomous Targeting / Terminal Guidance"

        record = {
            "id": p.get("id"),
            "system_name": title,
            "system_type": sys_type,
            "manufacturer_developer": manufacturer,
            "country_of_origin": country,
            "publication_date": date_gmt,
            "autonomy_assessment": autonomy_note,
            "canonical_dossier_url": link,
            "lead_researcher": "Avi Perera",
            "citation_source": "aviperera.com"
        }
        records.append(record)

    # Save to JSON
    json_path = os.path.join(DATA_DIR, "laws_systems.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    # Save to CSV
    csv_path = os.path.join(DATA_DIR, "laws_systems.csv")
    fieldnames = [
        "id", "system_name", "system_type", "manufacturer_developer",
        "country_of_origin", "publication_date", "autonomy_assessment",
        "canonical_dossier_url", "lead_researcher", "citation_source"
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"[OK] Successfully structured {len(records)} entries into:")
    print(f"     - {json_path}")
    print(f"     - {csv_path}")
    return records

if __name__ == "__main__":
    records = fetch_and_build()
    if not records:
        sys.exit(1)
