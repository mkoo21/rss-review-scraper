from . import PUBLISHED_TODAY, STRINGIFY, YESTERDAY
from bs4 import BeautifulSoup
from datetime import datetime
import feedparser
import re
import requests


def matches_category(entry, category):
    try:
        return bool(re.search(category, entry.category))
    except AttributeError:
        return False


def filter_by_category(category_name, entries):
    entries = list(entries)
    matches = list(filter(
        lambda x: matches_category(x, category_name),
        entries
    ))
    return "<h2>New Yorker / {} - {} results</h2>"\
           .format(category_name, len(matches)) + \
           "".join(list(map(lambda x: STRINGIFY(x, 'New Yorker'), matches)))


def get_magazines():
    msg = ""
    d = feedparser.parse('https://www.newyorker.com/feed/magazine/rss')
    pub_today = filter(PUBLISHED_TODAY, d.entries)

    msg += filter_by_category('The Current Cinema', pub_today)
    msg += filter_by_category('The Theatre', pub_today)
    return msg


def get_culture():
    msg = ""
    d = feedparser.parse('https://www.newyorker.com/feed/culture')
    pub_today = filter(PUBLISHED_TODAY, d.entries)

    msg += filter_by_category('The Front Row', pub_today)
    msg += filter_by_category('On Television', pub_today)
    return msg


def get_books():
    d = feedparser.parse('https://www.newyorker.com/feed/books')
    pub_today = filter(PUBLISHED_TODAY, d.entries)
    return filter_by_category('Books', pub_today)


def stringify_podcast(x):
    return "<p><b>{}</b></p><p> - New Yorker</p>\
            <p>https://www.newyorker.com{}</p>\
            <p>{}</p>".format(x.select_one('h4').text,
                              x.select_one('a')['href'],
                              x.select_one('h5').text)


def get_podcasts():
    req = requests.get('https://www.newyorker.com/culture/podcast-dept')
    doc = BeautifulSoup(req.content, 'html.parser')
    list_items = doc.select('li[class^=River__riverItem]')
    pub_today = list(filter(lambda x:
                            datetime.strptime(x.select_one('h6').text,
                                              '%B %d, %Y').date() >=
                            YESTERDAY.date(), list_items))

    return "<h2>New Yorker / Podcasts - {} results</h2>"\
           .format(len(pub_today)) + \
           "".join(list(map(lambda x: stringify_podcast(x), pub_today)))


def NEW_YORKER():
    return get_magazines() + get_culture() + get_books() + get_podcasts()
