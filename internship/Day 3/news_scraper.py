# news_scraper.py

import requests
from bs4 import BeautifulSoup
import argparse
import logging
from datetime import datetime

# ----------------- Logging Setup -----------------
logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ----------------- Keyword Filter -----------------
KEYWORDS = ["India", "Technology", "World", "Education", "Health"]

# ----------------- CLI Argument Parsing -----------------
parser = argparse.ArgumentParser(description="Scrape headlines from a news site.")
parser.add_argument('--url', type=str, default='https://www.bbc.com/news', help='Target news website URL')
args = parser.parse_args()
url = args.url

# ----------------- Fetch HTML -----------------
headers = {
    'User-Agent': 'Mozilla/5.0'
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    logging.error(f"Request failed: {e}")
    print("❌ Failed to fetch the website. See scraper.log for details.")
    exit()

# ----------------- Parse HTML -----------------
soup = BeautifulSoup(response.content, 'html.parser')
headlines = soup.find_all(['h2', 'h3'])

# ----------------- Filter & Save -----------------
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f"headlines_{timestamp}.txt"
count = 0

with open(filename, "w", encoding='utf-8') as f:
    for headline in headlines:
        text = headline.get_text(strip=True)
        if text and any(keyword.lower() in text.lower() for keyword in KEYWORDS):
            count += 1
            f.write(f"{count}. {text}\n")

if count == 0:
    print("⚠️ No matching headlines found with given keywords.")
else:
    print(f"✅ {count} filtered headlines saved to '{filename}'")

logging.info(f"Scraped {count} headlines from {url}")
