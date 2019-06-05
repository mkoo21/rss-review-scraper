from . import YESTERDAY, PST_TIMEZONE
from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta
import requests


def STRINGIFY(article):
    return "<p><b>{}</b> - THR </p><p>{}</p><p><em>{}</em></p>".format(
           article.a['data-pgm-title'],
           article.a['data-pgm-url'],
           article.find_all('a')[3].text)


def PUBLISHED_TODAY(article):
    date = datetime.strptime(
            article.footer.time['datetime'],
            '%Y-%m-%dT%H:%M:%S'
           )
    date = date.replace(tzinfo=PST_TIMEZONE)
    return date > YESTERDAY


def get_tv_reviews():
    req = requests.get('https://www.hollywoodreporter.com/topic/tv-reviews')
    articles = BeautifulSoup(req.content, 'html.parser').find_all('article')
    pub_today = list(filter(PUBLISHED_TODAY, articles))
    return "<h2>THR TV Reviews - {} results</h2>".format(len(pub_today)) + \
           "".join(list(map(STRINGIFY, pub_today)))


def get_movie_reviews():
    req = requests.get('https://www.hollywoodreporter.com/topic/movie-reviews')
    articles = BeautifulSoup(req.content, 'html.parser').find_all('article')
    pub_today = list(filter(PUBLISHED_TODAY, articles))
    return "<h2>THR Movie Reviews - {} results</h2>".format(len(pub_today)) + \
           "".join(list(map(STRINGIFY, pub_today)))


def THR():
    return get_tv_reviews() + get_movie_reviews()
