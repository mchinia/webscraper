# 🕷️ Smart Selenium Web Scraper

A **smart and adaptive web scraper** built with **Python + Selenium**, capable of automatically detecting the type of website (e.g., YouTube, Amazon, blogs) and applying **site-specific CSS selectors** to extract useful data — all with minimal setup.

---

## 🚀 Features

* 🔍 **Automatic site detection** — intelligently identifies YouTube, Amazon/Jumia/eBay, news/blogs, or generic sites.
* 🧠 **Dynamic selector mapping** — uses the right CSS selectors for each domain type.
* 📜 **Auto-scroll support** — scrolls pages multiple times to load dynamic content.
* ⚙️ **Headless mode** — runs silently in the background for efficient scraping.
* 💾 **Excel export** — automatically saves extracted data to `output.xlsx`.
* 🪄 **Plug-and-play simplicity** — just run and input any URL!

---

## 🧩 Supported Website Types

| Website Type         | Example Domains                                   | Data Extracted                   |
| -------------------- | ------------------------------------------------- | -------------------------------- |
| **YouTube**          | `youtube.com`                                     | Video titles, views, upload date |
| **E-commerce**       | `amazon.com`, `jumia.co.ke`, `ebay.com`           | Product name, price, rating      |
| **News / Blogs**     | `medium.com`, domains containing "blog" or "news" | Headline, author, date           |
| **Generic Websites** | Any other site                                    | Titles (h1-h3), paragraphs       |

---

## 📦 Requirements

* Python 3.8+
* Google Chrome
* The following Python packages:

```bash
pip install selenium webdriver-manager pandas openpyxl
```

---

## 🧰 How It Works

1. **Input a URL** when prompted.
2. The script detects the site type and chooses suitable **CSS selectors**.
3. It launches a **headless Chrome browser**.
4. The script **scrolls down** the page multiple times to load all content.
5. It **extracts and cleans** text data from matching elements.
6. Finally, results are **saved to an Excel file** (`output.xlsx`).

---

## 🖥️ Usage

### Run from Terminal or Command Prompt

```bash
python smart_scraper.py
```

Then input your desired URL when prompted:

```
🔗 Enter the website URL to scrape: https://www.youtube.com/@TechGuy
```

After scraping completes, the data will be saved as:

```
✅ Data saved to output.xlsx
```

---

## 🧪 Example Output (YouTube)

| Title                    | Views     | Uploaded    |
| ------------------------ | --------- | ----------- |
| How to Learn Python Fast | 54K views | 2 weeks ago |
| Automate with Selenium   | 23K views | 1 month ago |

---

## ⚠️ Notes

* Dynamic sites may require increasing the `wait_time` or `scroll_times` values.
* Some pages may use different element structures — adjust the selectors in `get_selectors_for_site()` if needed.
* For pages requiring login or JavaScript-heavy loading, consider manual cookies or Selenium waits.

---

## 🧑‍💻 Author

**Sandra Mchinia**
💼 *Nursing student | Aspiring AI Developer | Python Enthusiast*
🌍 Based in Nyeri, Kenya

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use, modify, and share.

---
### ⚖️ Disclaimer

This tool is intended for **educational and personal research use only**.  
It is **not affiliated with or endorsed by YouTube, Amazon, Medium, or any other mentioned platforms**.  
Users are responsible for ensuring their scraping activities comply with each website’s **Terms of Service** and **robots.txt** policies.
---
