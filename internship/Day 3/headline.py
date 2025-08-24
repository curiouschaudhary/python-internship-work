# news_scraper.py

import requests
from bs4 import BeautifulSoup

# Choose your target URL
url = 'https://www.bbc.com/news'

# Add headers (to simulate a browser visit)
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Send GET request
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <h3> or other headline tags (adjust as per the website)
headlines = soup.find_all(['h3', 'h2'])

# Save to a text file
with open("headlines.txt", "w", encoding='utf-8') as f:
    for i, headline in enumerate(headlines, 1):
        text = headline.get_text(strip=True)
        if text:
            f.write(f"{i}. {text}\n")

print("✅ Headlines saved to 'headlines.txt'")
