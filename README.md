# 📘 README – Kansas Businesses Scraping Project

## 📌 Project Overview
This project extracts business information for Kansas from **Enigma Business Directory**.

The pipeline works in two stages:

1. **Link Scraping** – Collects website links for the given category: `{category}`.
2. **Business Scraping** – Visits each website and extracts:
   - Business Name
   - Email(s)
   - Phone Number
   - Website
   - Address
   - Source URL
   - Category

Final structured output is saved as:  
**{output_file}**

---

## 📂 Deliverables
1. **Python Script(s)**  
   - `kansas_scraper.py` → End-to-end scraper for links + details.

2. **Excel Files**
   - `kansas_businesses.xlsx` → Raw scraped links.  
   - `{output_file}` → Final output with detailed business info.

3. **README File (this file)**  
   - Describes sources, missing categories, and challenges.

---

## 🛠️ Setup Instructions
1. Install dependencies:
```bash
pip install requests beautifulsoup4 pandas openpyxl
Run the scraper:

bash
Copy code
python kansas_scraper.py
Enter category when prompted (example):

Copy code
educational-institution/
Output file will be saved as:

Copy code
{output_file}
##🌐 Websites / Sources Used
Enigma Business Directory
{source_url}

##🚨 Missing Categories / Limitations
Some categories may not have enough businesses listed.

Some businesses hide emails → fewer results.

If less than 10 businesses are found, the output file includes a note:
"Less than 10 record available for this category".

##⚠️ Challenges Faced
Dynamic content loading (JavaScript not supported by BeautifulSoup).

Hidden or obfuscated emails (e.g., info [at] company dot com).

Duplicate business entries.

Websites blocking scrapers → required User-Agent headers.

Different page structures across sites.

##✅ Example Output (Excel)
Business Name	Email	Phone	Website	Address	Source URL	Category
ABC Coaching	info@abccoach.com	(123) 456-7890	https://abccoach.com	123 Main St, Kansas City	Enigma URL	Coaching Institutes
XYZ Academy	contact@xyz.com	(987) 654-3210	https://xyzacademy.com	45 Elm St, Wichita, KS	Enigma URL	Coaching Institutes

##📅 Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

python
Copy code
with open("README.txt", "w", encoding="utf-8") as f:
    f.write(readme_content.strip())

print("✅ README.txt file generated successfully.")
if name == "main":
# Example usage (you can pass real values after scraping)
category = "educational-institution/"
source_url = "https://www.enigma.com/directory/ks/all-cities/educational-institution/"
output_file = "Output_Kansas_educational_institution_scraped_data.xlsx"
