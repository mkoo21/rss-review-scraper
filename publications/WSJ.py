from . import YESTERDAY, PST_TIMEZONE
from bs4 import BeautifulSoup
from datetime import datetime
import re
import requests


def STRINGIFY(article):
    return "<p><b>{}</b> - WSJ </p><a>{}</a><em>{}</em>".format(
           article.find_all('div')[2].a,
           article.find_all('div')[0].a['href'],
           article.find_all('p')[1].text)


def PUBLISHED_TODAY(article):
    datestr = article.find_all('div')[2].div.p.text
    date = datetime.strptime(re.match(r'(.+) \w{2,} \w{2,}', datestr)[1], '%B %d, %Y %H:%M')
    date = date.replace(tzinfo=PST_TIMEZONE)
    return date > YESTERDAY


def WSJ():
    req = requests.get('https://www.wsj.com/news/author/joe-morgenstern')
    doc = BeautifulSoup(req.content, 'html.parser')

    articles = list(filter(PUBLISHED_TODAY, doc.find_all('article')))
    # print(list(map(STRINGIFY, filter(PUBLISHED_TODAY, articles))))
    return "<h2>WSJ Joe Morgenstern - {} results</h2>".format(len(articles)) + \
           "".join(list(map(STRINGIFY, articles)))
