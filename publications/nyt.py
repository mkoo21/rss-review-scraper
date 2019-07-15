from . import PUBLISHED_TODAY, STRINGIFY
import feedparser
import re

# Regular rss feeds (no additional processing)
URLS = {
    "NYT Television": "https://rss.nytimes.com/services/xml/rss/nyt/Television.xml",
    "NYT Theater": "https://rss.nytimes.com/services/xml/rss/nyt/Theater.xml"
}

# Movie reviews seem to be published with 'Review:' in the title - 05/31/19
MOVIE_URL = {
    "NYT Movie Reviews": "https://rss.nytimes.com/services/xml/rss/nyt/Movies.xml"
}

# Book reviews seem to preprend 'review' to the title in the url - 05/31/19
BOOKS_URL = {
    "NYT Book Reviews": "https://rss.nytimes.com/services/xml/rss/nyt/Books.xml"
}


def MOVIE_REVIEW(entry):
    return bool(re.search('review:', entry['title'], re.IGNORECASE))


def BOOK_REVIEW(entry):
    return bool(re.search('/books/review-', entry['link'], re.IGNORECASE))


def get_vanilla_rss():
    msg = ""
    for feed in URLS:
        d = feedparser.parse(URLS[feed])
        entries = list(filter(PUBLISHED_TODAY, d.entries))
        if len(entries) == 0:
            return ""
        msg += "<h2>{} - {} results</h2>".format(feed, len(entries)) + \
               "".join(list(map(lambda x: STRINGIFY(x, 'NYT'), entries)))
    return msg


def get_movies():
    msg = ""
    for feed in MOVIE_URL:
        d = feedparser.parse(MOVIE_URL[feed])
        pub_today = list(filter(PUBLISHED_TODAY, d.entries))
        is_review = list(filter(MOVIE_REVIEW, pub_today))
        if len(is_review) == 0:
            return ""
        msg += "<h2>{} - {} results</h2>".format(feed, len(is_review)) + \
               "".join(list(map(lambda x: STRINGIFY(x, 'NYT'), is_review)))
    return msg


def get_books():
    msg = ""
    for feed in BOOKS_URL:
        d = feedparser.parse(BOOKS_URL[feed])
        pub_today = list(filter(PUBLISHED_TODAY, d.entries))
        is_review = list(filter(BOOK_REVIEW, pub_today))
        if len(is_review) == 0:
            return ""
        msg += "<h2>{} - {} results</h2>".format(feed, len(is_review)) + \
               "".join(list(map(lambda x: STRINGIFY(x, 'NYT'), is_review)))
    return msg


def NYT():
    return get_vanilla_rss() + get_movies() + get_books()
