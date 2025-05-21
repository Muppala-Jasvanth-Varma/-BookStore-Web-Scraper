import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import json
import os

# Setup logging
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Base URL for the books site
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def get_last_page():
    """Dynamically find the total number of pages to scrape."""
    url = BASE_URL.format(1)
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    # Find the total number of pages from the pagination element
    try:
        page_text = soup.find("li", class_="current").text.strip()
        last_page = int(page_text.split()[-1])
        logging.info(f"Found total pages: {last_page}")
        return last_page
    except Exception as e:
        logging.error(f"Error finding total pages: {e}")
        return 5  # Default to 5 pages if error occurs

def scrape_page(page_num):
    """Scrape a single page and return a list of book dictionaries."""
    url = BASE_URL.format(page_num)
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
    except requests.RequestException as e:
        logging.error(f"Failed to fetch page {page_num}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    page_books = []

    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    for book in books:
        try:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.replace("£", "").strip()
            availability = book.find("p", class_="instock availability").text.strip()
            rating_class = book.p["class"][1]  # e.g., "Three"
            rating = rating_map.get(rating_class, 0)

            page_books.append({
                "Title": title,
                "Price (£)": float(price),
                "Rating": rating,
                "Availability": availability
            })
        except Exception as e:
            logging.warning(f"Error parsing book on page {page_num}: {e}")
            continue

    return page_books

def save_data(data, excel_path="output/books.xlsx", json_path="output/books.json"):
    """Save scraped data to Excel and JSON formats."""
    os.makedirs(os.path.dirname(excel_path), exist_ok=True)
    
    # Save to Excel
    df = pd.DataFrame(data)
    df.to_excel(excel_path, index=False)
    logging.info(f"Data saved to {excel_path}")

    # Save to JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    logging.info(f"Data saved to {json_path}")
def main():
    all_books = []
    total_pages = get_last_page()

    for page_num in range(1, total_pages + 1):
        print(f"Scraping page {page_num} of {total_pages}...")
        books_on_page = scrape_page(page_num)
        all_books.extend(books_on_page)

    save_data(all_books)
    print("✅ Scraping complete! Data saved to output/books.csv and output/books.json")

if __name__ == "__main__":
    main()
