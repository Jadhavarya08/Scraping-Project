# code to scrap teh web links 

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
url = "https://www.enigma.com/directory/ks/all-cities/educational-institution/"

# Send HTTP GET request
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Parse the page
soup = BeautifulSoup(response.text, "html.parser")

# Extract all <a> tags
links = []
for a in soup.find_all("a", href=True):
    href = a["href"]
    # Filter: only keep links starting with http and containing domain (company websites)
    if href.startswith("http") and "enigma.com" not in href:
        links.append(href)

# Remove duplicates
links = list(set(links))

# Save to Excel
df = pd.DataFrame(links, columns=["Website"])
df.to_excel("Coaching Institutes.xlsx", index=False)

print(f"✅ Scraped {len(links)} website links and saved to Kansas_Beauty&PersonalCare.xlsx")