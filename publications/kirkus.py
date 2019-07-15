from . import YESTERDAY
from bs4 import BeautifulSoup
from datetime import datetime
import re
import requests

req = requests.get('https://www.kirkusreviews.com/book-reviews/fiction-books-literature/?sort=published&availability=recent-reviews&stars=only')
doc = BeautifulSoup(req.content, 'html.parser')


def STRINGIFY(article):
    return "<p><b>{}</b> - Kirkus</p><p>{}</p><p><em>{}</em></p>".format(
           article.find("span", {"itemprop": "name"}).text,
           "https://www.kirkusreviews.com" + article.find("a", {"itemprop": "url"})['href'],
           re.search(r"\s+(.+)\s+", article.find('div', {'class': 'book-item-review-first'}).text)[1]

    )


def PUBLISHED_TODAY(article):
    review_date = article.find_all('div', {'class': 'hidden-xs book-item-meta'})[2].text
    date = datetime.strptime(
        re.match(r'Reviewed\: (.+)', review_date)[1],
        '%B %d, %Y').date()
    return date >= YESTERDAY.date()


def KIRKUS():
    books = doc.find_all("div", {"class": "row book-item-ctr"})
    pub_today = list(filter(PUBLISHED_TODAY, books))
    if len(pub_today) == 0:
        return ""
    return "<h2>Kirkus - {} results</h2>".format(len(pub_today)) + \
           "".join(list(map(STRINGIFY, pub_today)))
