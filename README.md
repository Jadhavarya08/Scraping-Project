📘 Kansas Businesses Scraping Project
📌 Project Overview

This project extracts business information for Kansas from the Enigma Business Directory
.

The workflow:

Scrape Links – Collects business website links for a given category.

Scrape Details – Visits each website and extracts details such as:

Business Name

Email(s)

Phone Number

Website

Address

Source URL

Category

Final results are stored in structured Excel files.

📂 Deliverables

Scripts

kansas_scraper.py → End-to-end scraper for links and details.

generate_readme.py → Generates this README file automatically.

Excel Files

kansas_businesses.xlsx → Raw scraped links.

Output_Kansas_<Category>_scraped_data.xlsx → Final detailed business data.

README.md

Project overview, setup, sources, challenges, and examples.

🛠️ Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/kansas-business-scraper.git
cd kansas-business-scraper

2. Install Dependencies
pip install requests beautifulsoup4 pandas openpyxl

3. Run the Scraper
python kansas_scraper.py

4. Enter Category

Example input:

educational-institution/

5. Output File
Output_Kansas_educational_institution_scraped_data.xlsx

🌐 Websites / Sources Used

Enigma Business Directory

🚨 Missing Categories / Limitations

Some categories may not have enough businesses listed.

Many businesses hide emails (e.g., use forms instead).

If fewer than 10 businesses are found, the Excel output includes a note:
"Less than 10 record available for this category".

⚠️ Challenges Faced

Dynamic content loading → Some pages use JavaScript, not supported by BeautifulSoup.

Obfuscated emails → e.g., info [at] company dot com.

Duplicates → Filtered out during scraping.

Scraper blocking → Required using headers (User-Agent).

Varied page structures → Different websites required flexible selectors.

✅ Example Output (Excel)
Business Name	Email	Phone	Website	Address	Source URL	Category
ABC Coaching	info@abccoach.com
	(123) 456-7890	https://abccoach.com
	123 Main St, Kansas City	Enigma URL	Coaching Institutes
XYZ Academy	contact@xyz.com
	(987) 654-3210	https://xyzacademy.com
	45 Elm St, Wichita, KS	Enigma URL	Coaching Institutes
