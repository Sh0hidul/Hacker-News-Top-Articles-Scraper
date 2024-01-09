# Hacker-News-Top-Articles-Scraper
This Python script scrapes the top articles from Hacker News and displays the titles, links, and scores of the top 5 articles. It utilizes the requests library for making HTTP requests and BeautifulSoup for HTML parsing.
Features
Retrieves the HTML content of the Hacker News homepage.
Parses the HTML content to extract information about the top articles, including titles, links, and scores.
Organizes the extracted data into a list of tuples.
Sorts the list based on article scores in descending order.
Prints the details of the top 6 articles.
Dependencies
Requests: Used for making HTTP requests.
BeautifulSoup: A library for pulling data out of HTML and XML files.

##  How to Use
Clone the repository:

git clone https://github.com/your-username/hacker-news-scraper.git
Install the required dependencies:

pip install -r requirements.txt
Run the script:

python hacker_news_scraper.py
