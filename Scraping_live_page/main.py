# Import required libraries
import requests
from bs4 import BeautifulSoup
from operator import itemgetter

# Send an HTTP GET request to the specified URL
response = requests.get("https://news.ycombinator.com/")

# Retrieve the HTML content of the requested page
content = response.text
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Initialize an empty list to store article data
article_data = []

# Find all elements with class 'titleline' (titles and links) and 'score' (article scores)
titleline = soup.find_all(class_='titleline')
article_score = soup.find_all(class_='score')

# Iterate over the titleline and article_score using zip
for title, point in zip(titleline, article_score):
    # Extract the numerical score from the article score text
    article_score1 = point.get_text().split(" ")
    score = int(article_score1[0])

    # Extract the article title and link
    article = title.get_text()
    article_link = title.a['href']

    # Append a tuple containing the score, title, and link to the article_data list
    article_data.append((score, article, article_link))

# Sort the article_data list based on the first element (score) in descending order
article_data.sort(key=itemgetter(0), reverse=True)

# Print the details of the top 5 articles
for article in article_data[:5]:
    print(article)
