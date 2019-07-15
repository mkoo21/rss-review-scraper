from . import YESTERDAY
from bs4 import BeautifulSoup
from datetime import datetime
import requests


def get_pubdate(article):
    try:
        return datetime.strptime(article.footer.time['datetime'], '%Y-%m-%dT%H:%M:%S%z')
    except (AttributeError, KeyError):
        return None


def STRINGIFY(article):
    return "<p><b>{}</b> - Variety</p><p>{}</p>".format(article.h3.a.text, article.a['href'])


def get_articles(t):
    page = requests.get('https://variety.com/v/{}/reviews/'.format(t))
    document = BeautifulSoup(page.content, 'html.parser')
    articles = document.find_all('article')
    pub_today = list(filter(lambda x: bool(get_pubdate(x)) and get_pubdate(x) >
                            YESTERDAY, articles))
    if len(pub_today) == 0:
        return ""
    return "<h2>Variety / {} - {} results</h2>".format(t, len(pub_today)) + \
           "".join(map(lambda x: STRINGIFY(x), pub_today))


def VARIETY():
    return get_articles('film') + get_articles('tv')
