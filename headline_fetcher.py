import requests
from bs4 import BeautifulSoup

def fetch_headlines():
    url = "https://arthalogy.com"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print("❌ Failed to fetch:", e)
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    # marquee tag
    marquee_div = soup.find("div", class_="marquee-content")
    if not marquee_div:
        print("⚠️ Marquee content not found.")
        return []

    # Extracting headlines
    headlines = []
    for item in marquee_div.find_all("span"):
        text = item.get_text(strip=True)
        if len(text) > 20: 
            headlines.append(text)

    return headlines[0]


