README – Kansas Businesses Scraping Project
📌 Project Overview

This project extracts business information for Kansas from Enigma Business Directory (https://www.enigma.com/directory/ks/
).
The pipeline works in two stages:

scrape_links.py – Scrapes business website links for a given category (e.g., educational institutions, coaching institutes, etc.) and saves them into an Excel file.

scrape_single_page.py – Visits each business website, extracts details (name, email, phone, address, etc.), and saves them into a structured Excel sheet.

The output can then be used for analysis, marketing, or category-wise business listing.

📂 Deliverables

Python Scripts

scrape_links.py → Scrapes links from Enigma directory pages.

scrape_single_page.py → Scrapes details from each collected website.

Excel Files

kansas_businesses.xlsx → Contains scraped links of businesses from the category page.

Output_Kansas_<Category>_scraped_data.xlsx → Contains full business details (emails, phone, etc.).

README File (this file)

Describes sources, instructions, missing categories, and challenges.

🛠️ Setup Instructions
1. Install Dependencies

Make sure Python 3.x is installed.
Then install required libraries:

pip install requests beautifulsoup4 pandas openpyxl

2. Run the Scripts

Step 1 – Scrape Links

python scrape_links.py


This saves an Excel file named kansas_businesses.xlsx (or Coaching Institutes.xlsx if running the demo).

Step 2 – Scrape Business Details

python scrape_single_page.py


The script will ask for a category name (e.g., "Coaching Institutes").

It will read kansas_businesses.xlsx, visit each link, and extract:

Business Name

Email(s)

Phone Number

Website

Address

Source URL

Category

Final structured output is saved as:

Output_Kansas_<Category>_scraped_data.xlsx

🌐 Websites / Sources Used

Enigma Business Directory: https://www.enigma.com/directory/ks/

(e.g., https://www.enigma.com/directory/ks/all-cities/educational-institution/
)

📊 Data Fields Collected

Business Name

Email(s)

Phone Number

Website

Address

Source URL (where scraped from)

Category

🚨 Missing Categories / Limitations

Some categories may not have enough businesses listed.

Some businesses do not expose emails publicly → fewer email results.

A few websites block scrapers or load content dynamically → data not extracted.

If less than 10 businesses are found for a category, the output file will contain a message row:
"Less than 10 record available for this category".

⚠️ Challenges Faced

Dynamic content: Some websites load details with JavaScript → not captured by BeautifulSoup.

Hidden/Obfuscated emails: Many sites use formats like info [at] company dot com, which required regex + replacements.

Duplicate entries: Multiple links to the same business had to be filtered out.

Rate limiting / blocks: Some websites block automated scrapers, so User-Agent headers were added.

Data inconsistencies: Different websites use different layouts → extraction logic had to cover multiple selectors.

✅ Output Example (Excel)
Business Name	Email	Phone	Website	Address	Source URL	Category
ABC Coaching	info@abccoach.com
	(123) 456-7890	https://abccoach.com
	123 Main St, Kansas City, KS	Enigma URL	Coaching Institutes
XYZ Academy	contact@xyz.com
	(987) 654-3210	https://xyzacademy.com
	45 Elm St, Wichita, KS	Enigma URL	Coaching Institutes
📌 Notes

All scripts include comments explaining each step.

Output is Excel-compatible (.xlsx) for easy analysis.

Can be extended to multiple categories by changing the base URL and category input.# Scraping-Project
This project extracts business information for Kansas from Enigma Business Directory
