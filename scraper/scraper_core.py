import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import certifi
import certifi_win32  # Enables Windows certificate support
import schedule
import time
from datetime import datetime

# ========== CONFIGURATION ==========
BASE_URL = "https://www.ibps.in/career/"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = OUTPUT_DIR / "scraper_log.txt"

# ========== LOGGING ==========
def log_message(message: str):
    """Write log messages to both console and a text log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] {message}"
    print(formatted_message)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted_message + "\n")

# ========== SCRAPER CORE ==========
def scrape_ibps_jobs():
    """Scrape IBPS Career page and extract job information."""
    log_message("🔍 Fetching IBPS Career page...")

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(BASE_URL, timeout=10, headers=headers, verify=certifi.where())
    except requests.exceptions.SSLError:
        log_message("⚠️ SSL verification failed — retrying without SSL verification...")
        response = requests.get(BASE_URL, timeout=10, headers=headers, verify=False)

    if response.status_code != 200:
        log_message(f"❌ Failed to load page (Status Code: {response.status_code})")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for link in soup.find_all("a"):
        href = link.get("href")
        title = link.get_text(strip=True)

        if not href or not title:
            continue

        # Match relevant keywords to identify job-related links
        keywords = ["pdf", "crp", "recruitment", "advertisement", "notification", "important notice"]
        if any(kw in href.lower() or kw in title.lower() for kw in keywords):
            if not href.startswith("http"):
                href = f"https://www.ibps.in/{href.lstrip('/')}"
            
            # Extract pseudo date or location if available in title
            date = None
            location = "All India"
            for word in title.split():
                if any(ch.isdigit() for ch in word) and "/" in word:
                    date = word  # crude date detection (e.g., 01/11/2025)
                    break

            jobs.append({
                "Job Title": title,
                "Location": location,
                "Publish Date": date or "N/A",
                "Link": href
            })

    # Remove duplicates
    jobs = [dict(t) for t in {tuple(d.items()) for d in jobs}]
    log_message(f"✅ Found {len(jobs)} job postings.")

    if jobs:
        df = pd.DataFrame(jobs)
        csv_path = OUTPUT_DIR / "ibps_jobs.csv"
        json_path = OUTPUT_DIR / "ibps_jobs.json"
        df.to_csv(csv_path, index=False)
        df.to_json(json_path, orient="records", indent=4)
        log_message(f"📁 Saved results to: {csv_path}")
        log_message(f"📁 Saved results to: {json_path}")
    else:
        log_message("⚠️ No job listings found — check IBPS site structure.")

    return jobs

# ========== SCHEDULER ==========
def run_scheduler():
    """Automatically scrape weekly (every Monday 9 AM)."""
    schedule.every().monday.at("09:00").do(scrape_ibps_jobs)
    log_message("🕒 Scheduler started — will run every Monday at 9:00 AM.")

    while True:
        schedule.run_pending()
        time.sleep(60)

# ========== MAIN ==========
if __name__ == "__main__":
    scrape_ibps_jobs()  # Run immediately
    # Uncomment below line to enable automatic weekly scheduling
    # run_scheduler()
