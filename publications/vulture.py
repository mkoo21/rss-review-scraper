from bs4 import BeautifulSoup
import re
import requests

req = requests.get('https://www.vulture.com/news/review')
doc = BeautifulSoup(req.content, 'html.parser')


def STRINGIFY(article):
    return "<p><b>{}</b> - Vulture</p><p>{}</p><p><em>{}</em></p>".format(
        article['data-track-headline'],
        article.find('a')['href'],
        article.find('a').text
    )


def PUBLISHED_TODAY(article):
    # Check format of the publish date - articles published within 24 hours 
    # will say e.g. '6 hours ago' instead of listing a date
    return not bool(re.match(r'\d{,2}/\d{,2}/\d{4}', article.div.div.time.text))


def VULTURE():
    articles = list(filter(lambda x: x['class'] == ['article'], doc.find('section').ol.find_all('li')))
    pub_today = list(filter(PUBLISHED_TODAY, articles))
    if len(pub_today) == 0:
        return ""
    return "<h2>Vulture - {} results</h2>".format(len(pub_today)) + \
           "".join(list(map(STRINGIFY, pub_today)))
