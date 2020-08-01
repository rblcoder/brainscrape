# BrainyQuote Web Scraper (By Keyword)
# SPECIAL POMMUNISM EDITION
# Alaina Kafkes

import requests
from bs4 import BeautifulSoup
import time

example_key = "lemons"
example_author = "kurt_vonnegut"


def getQuotes(keyword=example_key, numpages=7):
    """
    Given a keyword and the number of HTML pages of quotes to parse, uses Requests & BeautifulSoup to obtain (quote, author) tuples from BrainyQuote.
    Returns list of (quote, author) tuples and the length of this list.
    """
    # Initialize lists
    quoteArray = []
    authorArray = []
    pageNameArray = [keyword+"-quotes"]
    for i in range(2, numpages + 1):
        pageNameArray.append(keyword + "-quotes" + "_" + str(i))

    # For every page pertaining to a topic
    for page in pageNameArray:
        time.sleep(5)
        # Obtain BrainyQuote page html
        base_url = "http://www.brainyquote.com/quotes/keywords/"
        url = base_url + page
        # print('url : ', url)
        # continue
        response_data = requests.get(url).text[:]
        soup = BeautifulSoup(response_data, 'html.parser')

        # Populate quoteArray
        for item in soup.find_all("a", title="view quote"):
            quoteArray.append(item.get_text().rstrip())

        # Populate authorArray
        for item in soup.find_all("a", title="view author"):
            authorArray.append(item.get_text())

    # Create list of tuples of the form (quote, author)
    ans = zip(quoteArray, authorArray)
    return ans  # , len(ans)


def getQuotesByAuthor(author=example_author, numpages=4):
    """
    Given the author name and the number of HTML pages of quotes to parse, uses Requests & BeautifulSoup to obtain (quote, author) tuples from BrainyQuote.
    Returns list of (quote, author) tuples and the length of this list.
    """
    # Initialize lists
    quoteArray = []
    authorArray = []
    pageNameArray = [author+"-quotes"]
    for i in range(2, numpages + 1):
        pageNameArray.append(author+ "-quotes" + "_" + str(i))

    # For every page pertaining to a topic
    for page in pageNameArray:
        time.sleep(5)
        # Obtain BrainyQuote page html
        base_url = "http://www.brainyquote.com/quotes/authors/"
        url = base_url + page
        # print('url : ', url)
        # continue
        response_data = requests.get(url).text[:]
        soup = BeautifulSoup(response_data, 'html.parser')

        # Populate quoteArray
        for item in soup.find_all("a", title="view quote"):
            quoteArray.append(item.get_text().rstrip())

        # Populate authorArray
        for item in soup.find_all("a", title="view author"):
            authorArray.append(item.get_text())

    # Create list of tuples of the form (quote, author)
    ans = zip(quoteArray, authorArray)
    return ans #, len(ans)

