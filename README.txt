||Web Scraping||

In this project, I scraped "http://books.toscrape.com", which is a scrape
friendly website. It is a fake online bookstore with a list of books
with their prices and user ratings.

BeautifulSoup module was used to parse the HTML content and requests module was
used for fetching the webpage.
Connection is established with an existing sqlite3 database and a two tables
are created, namely BOOKS and CATEGORY. BOOKS contains the following information:
Name of the book, price, availability, user rating, and a foreign key to map the
books to each category. CATEGORY contains the list of categories for the books.
