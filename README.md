# brainscrape

### BrainyQuote web scraper written in Python using Requests & BeautifulSoup

Ever wanted to search quotes by keyword and amass them in a organized, streamlined manner? Do you love discovering new aphorisms and quips to spice up your life?

Then brainscrape is great for you! Simply run:

```python
insp_quotes = getQuotes('inspiration', 2)
for q, author in insp_quotes:
    print(q)
    print(author)

confucius_quotes = getQuotesByAuthor('confucius', 2)
for q, author in confucius_quotes:
    print(q)
    print(author)
```

... and a lovely list of (quote, author) tuples will be bestowed upon you for further use.

This is just a proof-of-concept for now; don't hesitate to submit a pull request if you'd like to see other features. Hope you enjoy brainscrape!
