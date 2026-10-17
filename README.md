# 📚 Book Parser (://toscrape.com)
[![Languages & Frameworks](https://skillicons.dev/icons?i=python&theme=light)](https://skillicons.dev)

A lightweight, interactive command-line web scraper built with Python to automatically extract book data from [://toscrape.com](https://://toscrape.com/). The script efficiently handles multi-page pagination, validates user inputs, and exports clean datasets into a spreadsheet-ready format.

## 🚀 Key Features

* **Interactive Category Selection** – Dynamically fetches available genres and prompts the user to select one.
* **Smart Pagination Loop** – Automatically navigates through multiple pages (e.g., `page-2.html`, `page-3.html`) if the requested book count exceeds the 20-item single-page limit.
* **Input Validation & Safety** – Robust loops prevent program crashes due to spelling mistakes or entering numbers outside the valid range.
* **Excel-Friendly CSV Export** – Formats numeric price fields using regional decimal standards to prevent Excel from corrupting prices into calendar dates.

* ## 🛠️ Tech Stack

* **Python 3** – Core programming language.
* **Requests** – Handles HTTP requests and forces precise UTF-8 encoding.
* **BeautifulSoup4 (lxml parser)** – Traverses the HTML DOM tree rapidly to locate elements.
* **CSV (DictWriter)** – Streams and structures scraped dict rows into a flat file.

* ## 📦 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/eclipse-oss/book_parser
   cd book_parser
   ```

2. **Install required dependencies:**
   ```bash
   pip install requests beautifulsoup4 lxml
   ```

3. **Run the parser script:**
   ```bash
   python main.py
   ```

---

## 📊 Exported Data Structure Example

Upon successful completion, the script generates a `books.csv` file structured as follows:

| title | price | availability |
| :--- | :--- | :--- |
| Full Moon over Noah's Ark | 49,43£ | In stock |
| Shakespeare's Sonnets | 20,66£ | In stock |

<img width="506" height="732" alt="image" src="https://github.com/user-attachments/assets/1fbe4d78-704b-475e-9d96-8c6446ac493b" />
example of excel

## ⚙️ Console Demo

```text
Enter the topic or (type everything u want to leave):
sequential-art_5
How many books do you want to parse? (min: 1, max: 75):
25

All data has been hastily recorded!
```
<img width="1553" height="368" alt="image" src="https://github.com/user-attachments/assets/1b75f81c-70ad-43b2-87c0-889dcbf7f31e" />
<img width="1570" height="434" alt="image" src="https://github.com/user-attachments/assets/42fbfcc1-c92f-4c37-9a93-ca6e9fdffe1b" />
examples of console

