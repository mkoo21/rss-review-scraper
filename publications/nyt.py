from datetime import datetime
import feedparser

# Regular rss feeds (no additional processing)
URLS = {
    "NYT Television": "https://rss.nytimes.com/services/xml/rss/nyt/Television.xml",
    "NYT Theater": "https://rss.nytimes.com/services/xml/rss/nyt/Theater.xml"
}

# Movie reviews seem to be published with 'Review' in the title - 05/31/19
MOVIE_URL = {
    "NYT Movies": "https://rss.nytimes.com/services/xml/rss/nyt/Movies.xml"
}

# Book reviews seem to preprend 'review' to the title in the url - 05/31/19
BOOKIE_URL = {
    "NYT Books": "https://rss.nytimes.com/services/xml/rss/nyt/Books.xml"
}
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S %z'
TODAY = datetime.today().date()


def PUBLISHED_TODAY(entry):
    result = datetime.strptime(entry['published'], DATE_FORMAT).date() == TODAY
    return result


def STRINGIFY(entry):
    return "<p><b>{}</b> - NYT</p><p>{}</p><p>{}</p>".format(
            entry['title'],
            entry['link'],
            entry['description'])


def NYT():
    msg = ""
    for e in URLS:
        d = feedparser.parse(URLS[e])
        entries = list(filter(lambda x: PUBLISHED_TODAY(x), d.entries))
        msg += "<h2>{}</h2>".format(e) + \
               "".join(list(map(lambda x: STRINGIFY(x), entries)))
    return msg
