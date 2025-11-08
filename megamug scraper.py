from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from urllib.parse import urlparse
import time

def get_selectors_for_site(url):
    """Auto-detect website type and return suitable CSS selectors."""
    domain = urlparse(url).netloc.lower()

    # 🔹 YouTube channel or video pages
    if "youtube.com" in domain:
        return {
            "Title": "#video-title",
            "Views": "span.inline-metadata-item:nth-child(1)",
            "Uploaded": "span.inline-metadata-item:nth-child(2)"
        }

    # 🔹 Amazon or shopping sites (generic)
    elif "amazon" in domain or "jumia" in domain or "ebay" in domain:
        return {
            "Product Name": "h2 a span",
            "Price": "span.a-price-whole, span.prc",
            "Rating": "span.a-icon-alt"
        }

    # 🔹 News or blog sites
    elif "medium.com" in domain or "blog" in domain or "news" in domain:
        return {
            "Headline": "h1, h2, h3",
            "Author": ".author, .byline, span[itemprop='author']",
            "Date": "time, .date, .published"
        }

    # 🔹 Default fallback (generic)
    else:
        return {
            "Title": "h1, h2, h3",
            "Paragraphs": "p"
        }


def scrape_with_selenium(url, output_file="output.xlsx", wait_time=5, scroll_times=3):
    """Smart Selenium web scraper that auto-selects site-specific CSS selectors."""
    # Auto-select appropriate CSS selectors
    selectors = get_selectors_for_site(url)
    print(f"🧠 Auto-detected selectors for {url}:\n{selectors}\n")

    # Setup browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # runs in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)

    print(f"⏳ Loading page: {url}")
    time.sleep(wait_time)

    # Auto-scroll to load dynamic content
    for i in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(f"📜 Scrolled down {i + 1}/{scroll_times} times...")
        time.sleep(3)

    data = {}
    for label, selector in selectors.items():
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            data[label] = [el.text.strip() for el in elements if el.text.strip()]
        except Exception as e:
            print(f"⚠️ Error scraping {label}: {e}")
            data[label] = []

    driver.quit()

    # Handle unequal lengths
    if not data:
        print("❌ No data extracted.")
        return

    max_len = max(len(v) for v in data.values())
    for k in data:
        while len(data[k]) < max_len:
            data[k].append("")

    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"✅ Data saved to {output_file}")
    print(df.head())


# Run the scraper
if __name__ == "__main__":
    url = input("🔗 Enter the website URL to scrape: ").strip()
    scrape_with_selenium(url)
