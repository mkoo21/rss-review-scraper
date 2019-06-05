from . import FROM_FEED_PUBLISHED_TODAY, STRINGIFY


def filter_by_tag(tag, entries):
    matches = list(filter(
        lambda x: any(list(map(
            lambda y: y.term == tag,
            x.tags
            ))),
        entries
    ))
    return "<h2>TIME {} - {} results</h2>".format(tag, len(matches)) + \
           "".join(list(map(lambda x: STRINGIFY(x, 'TIME'), matches)))


def TIME():
    pub_today = FROM_FEED_PUBLISHED_TODAY('https://feeds2.feedburner.com/time/entertainment')
    return filter_by_tag('movies', pub_today) + \
        filter_by_tag('Television', pub_today)
