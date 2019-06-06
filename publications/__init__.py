from datetime import datetime, timedelta, timezone
import feedparser

PST_TIMEZONE = timezone(offset=timedelta(hours=-7))
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S %z'
TODAY = datetime.now(timezone.utc)
YESTERDAY = TODAY - timedelta(days=1)


def FROM_FEED_PUBLISHED_TODAY(feed):
    d = feedparser.parse(feed)
    return list(filter(PUBLISHED_TODAY, d.entries))


def PUBLISHED_TODAY(entry):
    try:
        return datetime.strptime(entry['published'], DATE_FORMAT) \
           > YESTERDAY
    except ValueError:
        print('RSS entry did not match date format: {}'.format(entry))
        return False


def STRINGIFY(entry, pub):
    return "<p><b>{}</b> - {}</p><p>{}</p><p>{}</p>".format(
            entry['title'],
            pub,
            entry['link'],
            entry['description'])
