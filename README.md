# BookStore Web Scraper


A beginner-friendly yet production-ready Python web scraping project that collects book data from BooksToScrape.com. The project dynamically scrapes all book titles, prices, ratings, and availability across multiple pages and stores the data in Excel and JSON formats.

##Features
🔁 Dynamic Pagination – Automatically detects the total number of pages to scrape.

🧠 BeautifulSoup + Requests – Efficient HTML parsing and data extraction.

📊 Excel & JSON Export – Clean output stored in output/books.xlsx and output/books.json.

✅ Robust Error Handling – Graceful failure with logging for debugging.

📄 Logging System – Generates a scraper.log file to trace scraping activities.

🧩 Modular Code – Clean, maintainable, and production-ready Python structure.

## Project Structure
bash
Copy
Edit
book-scraper/
│
├── output/
│   ├── books.xlsx           # Final Excel output
│   └── books.json           # Optional JSON output
│
├── scraper.log              # Logs scraping activity
├── requirements.txt         # Required Python libraries
└── start.py                 # Main scraping script
## Requirements
Python 3.7+

Libraries:

requests

beautifulsoup4

pandas

openpyxl (for Excel export)

Install all dependencies:
pip install -r requirements.txt

▶️ How to Run
python start.py

###The script will:

Crawl all available pages of books.

Extract: Title, Price, Rating (1–5), Availability.

Save data into output/books.xlsx and output/books.json.

### Sample Output Preview
Title	Price (£)	Rating	Availability
It's Only the Himalayas	45.17	2	In stock
The Bear and the Piano	36.89	4	In stock
Sophie's World	15.94	5	In stock

## Use Case Ideas
📈 Analyze price vs. rating using Python/Excel visualizations.

🧠 Learn fundamentals of web scraping.

🧑‍💻 Add as a mini project to your ML/Data Science/Backend portfolio.

###What You Learn
Navigating and parsing HTML using BeautifulSoup

Sending HTTP requests using Requests

Extracting data and saving it in structured formats

Writing clean, modular, and reusable code

Logging and exception handling for real-world apps

### Future Enhancements
⏰ Add scheduling for auto-scraping (using cron or schedule lib)

🌍 Add proxy/headers support to simulate real browser

📊 Create a dashboard or simple GUI

☁️ Push data to Google Sheets / Firebase / MongoDB

### Author
#Jasvanth Varma Muppala – Engineering Student | Aspiring Machine Learning Engineer
