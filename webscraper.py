import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "http://quotes.toscrape.com" 

# Send a request
response = requests.get(url)
print("Status code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote texts
quotes = soup.find_all("span", class_="text")

# Debug: check how many found
print("Number of quotes found:", len(quotes))

# Print first few quotes
for i, quote in enumerate(quotes[:5], 1):
    print(f"{i}. {quote.text}")

# Save to file
with open("quotes.txt", "w", encoding="utf-8") as file:
    for i, quote in enumerate(quotes, 1):
        file.write(f"{i}. {quote.text}\n")

print("Quotes saved to quotes.txt")
