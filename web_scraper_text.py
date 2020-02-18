# A simple web scraper for extracting (raw) text from a webpage.

# Importing modules (BeautifulSoup)
from bs4 import BeautifulSoup, SoupStrainer
import requests
import urllib
from urllib.request import urlopen, Request
import docx  # To install this, use pip install python_docx or pip install python-docx
# from docx import Document


# Choosing the url
url = "https://www.enchantedlearning.com/wordlist/water.shtml"

## headers defines a dummy browser for this program to use. Without it, an error occurs so you should use it!
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
# Request the url for scraping
req = Request(url=url, headers=headers)
html = urlopen(req).read() 
soup = BeautifulSoup(html, features="lxml")
    # kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

    # get raw text without line breaks etc.
text = soup.get_text()
    # break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("\n"))
    # drop blank lines
text = ' '.join(chunk for chunk in chunks if chunk)

print("\n", text)


# Writing to a text file
# (Remember to specify a path)

file1 = open("scraped_text.txt", "w", encoding = 'utf-8')
file1.write(text)
file1.close()
print("\nFinished writing to", file1)