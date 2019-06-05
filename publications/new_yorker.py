from . import PUBLISHED_TODAY, STRINGIFY
import feedparser
import re


def filter_by_category(category_name, entries):
    matches = list(filter(
        lambda x: bool(re.search(category_name, x.category)),
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


def NEW_YORKER():
    return get_magazines() + get_culture() + get_books()
