import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# The URL of the page you want to scrape
url = "https://www.immobiliare.it/annunci/108773485/"

# Use the requests library to get the content of the page
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Get all elements
all_elements = soup.find_all()

for element in all_elements:
    if element.text.strip():  # Check if the element has text content
        print(element.text.strip())  # Print the text content of each element, removing extra whitespace


# import requests
# from bs4 import BeautifulSoup

# # The URL of the page you want to scrape
# url = "https://www.immobiliare.it/annunci/108773485/"

# # Use the requests library to get the content of the page
# response = requests.get(url)

# # Use BeautifulSoup to parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Now you can use BeautifulSoup's methods to find the data you're interested in.
# # For example, to find all paragraphs, you could use:
# paragraphs = soup.find_all('p')

# # for paragraph in paragraphs:
# #     print(paragraph.text)
# for paragraph in paragraphs:
#     print(paragraph.text.encode('utf-8').decode('utf-8'))
    
# import requests
# from bs4 import BeautifulSoup

# # The URL of the page you want to scrape
# url = "https://www.immobiliare.it/annunci/108773485/"

# # Use the requests library to get the content of the page
# response = requests.get(url)

# # Use BeautifulSoup to parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Get all elements
# all_elements = soup.find_all()

# for element in all_elements:
#     print(element.name)  # This will print the name of each tag
