# Save as scrape_single_page.py
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

category = input("enter category")

EMAIL_RE = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}', re.I)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0; +https://yourdomain.example)"
}

def extract_emails(text):
    """Extract emails including some obfuscated ones."""
    emails = set(EMAIL_RE.findall(text))
    # Handle common obfuscations
    text2 = text.replace(' (at) ', '@').replace(' [at] ', '@').replace(' dot ', '.')
    emails |= set(EMAIL_RE.findall(text2))
    return list(emails)

def scrape_business_page(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    # Business name
    name = (soup.select_one("h1") or 
            soup.select_one(".business-name") or 
            soup.select_one(".merchant-name"))
    business_name = name.get_text(strip=True) if name else ""

    # Phone
    phone = (soup.select_one(".phone") or 
             soup.find(text=re.compile(r'\(\d{3}\)')))
    phone_text = phone.get_text(strip=True) if hasattr(phone, "get_text") else (phone or "")

    # Website link (may be same as url)
    website_link = None
    for a in soup.find_all("a", href=True):
        href = a['href']
        if 'http' in href and ('website' in a.get_text(strip=True).lower() or 'visit website' in a.get_text(strip=True).lower()):
            website_link = href
            break
    if not website_link:
        for a in soup.find_all("a", href=True):
            if 'http' in a['href'] and not a['href'].startswith('mailto:') and 'yelp' not in a['href']:
                website_link = a['href']
                break

    # Emails
    emails = extract_emails(r.text)
    for a in soup.select('a[href^=mailto]'):
        m = EMAIL_RE.search(a['href'])
        if m: emails.append(m.group(0))
    emails = list(dict.fromkeys(emails))  # dedupe preserving order

    # Address
    addr = ""
    addr_tag = (soup.select_one(".address") or 
                soup.select_one(".business-address") or 
                soup.find("address"))
    if addr_tag:
        addr = addr_tag.get_text(separator=", ", strip=True)

    return {
        "source_url": url,
        "business_name": business_name,
        "emails": emails,
        "phone": phone_text,
        "website": website_link or url,
        "address": addr
    }

if __name__ == "__main__":
    # Read input Excel
    input_file = "Coaching Institutes.xlsx"
    df = pd.read_excel(input_file)

    results = []
    seen = set()  # To skip duplicates

    for url in df['Website'].dropna():
        record = scrape_business_page(url)
        if record and record["emails"]:  # Skip if no email found
            for email in record["emails"]:
                key = (record["business_name"], email.lower())
                if key in seen:
                    continue
                seen.add(key)
                results.append({
                    "Business Name": record["business_name"],
                    "Email": email,
                    "Phone": record["phone"],
                    "Website": record["website"],
                    "Address": record["address"],
                    "Source URL": record["source_url"],
                    "Category" : category
                })

    # Save to Excel
    output_file = "Output_Kansas_Coaching Institutes_scraped_data.xlsx"
    out_df = pd.DataFrame(results)
    out_df = out_df.drop_duplicates(subset=["Website"])  # Remove duplicate websites

    # If less than 10 records, add a message row
    if len(out_df) < 10:
        # Create a DataFrame with the message (fill other columns with empty strings)
        msg_row = {col: "" for col in out_df.columns}
        msg_row["Business Name"] = "Less than 10 record available for this category"
        out_df = pd.concat([out_df, pd.DataFrame([msg_row])], ignore_index=True)

    out_df.to_excel(output_file, index=False)

    print(f"✅ Scraping complete. Saved {len(out_df)} records to {output_file}")
