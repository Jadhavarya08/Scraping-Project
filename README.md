# 🏢 Kansas Business Scraper

A Python-based web scraper that collects **business details in Kansas** from the  
[Enigma Business Directory](https://www.enigma.com/directory/ks/).

The scraper extracts:
- ✅ Business Name  
- ✅ Email(s)  
- ✅ Phone Number  
- ✅ Website  
- ✅ Address  
- ✅ Category & Source URL  

All results are saved into **Excel files** for easy analysis.

---

## ⚡ Features
- Scrapes business listings from a given **category**.  
- Cleans and stores data in structured **Excel (.xlsx)** format.  
- Handles **duplicates** automatically.  
- Adds a note if **less than 10 records** are found.  
- Built with **Requests + BeautifulSoup + Pandas**.  

---

## 📦 Installation

Clone the repository:


git clone https://github.com/your-username/kansas-business-scraper.git
cd kansas-business-scraper
Install dependencies:


pip install -r requirements.txt
Or install manually:


pip install requests beautifulsoup4 pandas openpyxl
## 🚀 Usage
- Run the scraper:


- python kansas_scraper.py
- When prompted, enter a category (example):


- educational-institution/

## 📂 Output
Results are saved as:


Output_Kansas_<category>_scraped_data.xlsx
Example:

Output_Kansas_educational-institution_scraped_data.xlsx

## 📊 Example Output (Excel)
Business Name	Email	Phone	Website	Address	Source URL	Category
ABC Coaching	info@abccoach.com	(123) 456-7890	https://abccoach.com	123 Main St, Kansas City	Enigma URL	Coaching Institutes
XYZ Academy	contact@xyz.com	(987) 654-3210	https://xyzacademy.com	45 Elm St, Wichita, KS	Enigma URL	Coaching Institutes

🌐 Sources
Enigma Business Directory

## ⚠️ Limitations
- Some categories may not have enough businesses.

- Many websites hide emails (forms or obfuscation).

- JavaScript-heavy sites are not supported (BeautifulSoup limitation).

- Website blocking may occur → handled using User-Agent headers.

## 🛠️ Challenges Faced
- Dynamic content loading

- Hidden / obfuscated emails

- Duplicate business entries

- Varied website structures

