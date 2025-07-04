
#This code is based youtube video: https://www.youtube.com/watch?v=IMccv8xbguE


import requests
from bs4 import BeautifulSoup

# Define the URL of the site to scrape
url = 'https://books.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all book entries - inspect the site to find the correct class for book items
books = soup.find_all('article', class_='product_pod')

# Loop through each book and extract information
for book in books:
    # Extract the title of the book
    title = book.find('h3').find('a')['title']
    
    # Extract the price of the book
    price = book.find('p', class_='price_color').text
    
    print(f'Title: {title}, Price: {price}')

