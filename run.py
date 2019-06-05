import ipdb
import json
from mail import send_mail
from publications.nyt import NYT
from publications.new_yorker import NEW_YORKER
from publications.time_mag import TIME
from publications.variety import VARIETY
from publications.WSJ import WSJ
from publications.THR import THR
from publications.vulture import VULTURE
from publications.kirkus import KIRKUS


def scrape_publication(f):
    try:
        return f()
    except Exception as e:
        ipdb.set_trace()
        return "<p>Encountered an issue with publication {}!</p><p>{}</p>".format(f.__name__, e.message)


def main(event=None, context=None):
    email_string = ""
    for pub in [NYT, NEW_YORKER, TIME, VARIETY, WSJ, THR, VULTURE, KIRKUS]:
        email_string += scrape_publication(pub)
    send_mail(email_string)

    return {
        'statusCode': 200,
        'body': json.dumps('Execution complete.')
    }