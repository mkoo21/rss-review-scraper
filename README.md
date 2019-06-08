## Review Scraper

The purpose of this project is to automatically retrieve reviews from a set of publications/links that were published in the past day, then to summarize the results in a digest email. 

## Project structure

The entrypoint is `run.py`, and the code for scraping individual publications is all in the `publications` folder for organization. Most of the publications have RSS feeds which you can filter for review results, but some need to be screen-scraped. Note that the RSS data is not error-free. 

As much as possible the scrapers will try to filter for pieces published in the past 24 hours, or where the date is today or yesterday. Articles seem to sometimes get edits, or be released after they are written, so the pubDate in the RSS feed is often a few days after the date listed in the article.

The first thing you _need_ to do is edit `mail.py` and set values for `EMAIL, PASS, RECIPIENT` to the email/password of a valid gmail account to be the sender for the digest email, and a recipient to which the email will be sent. 

## Installation/dependencies

Depencies are all listed in `requirements.txt`. I used a virtualenv but you can use whatever works for you. This project was deployed on AWS Lambda, but you can run it from cron as well with a venv.

If you know Python but are new to virtualenvs, read about them here: https://docs.python-guide.org/dev/virtualenvs/

But the gist of it is:

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

Then:

```
pip install -r requirements.txt
```

See https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html for instructions on how to deploy to Lambda.
