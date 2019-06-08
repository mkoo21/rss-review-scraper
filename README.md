## Review Scraper

The purpose of this project is to automatically retrieve reviews from a set of publications/links that were published in the past day, then to summarize the results in a digest email. 

## Project structure

The entrypoint is `run.py`, and the code for scraping individual publications is all in the `publications` folder for organization. Most of the publications have RSS feeds which you can filter for review results, but some need to be screen-scraped. Note that the RSS data is not error-free.

The first thing you _need_ to do is edit `mail.py` and set values for `EMAIL, PASS, RECIPIENT` to the email/password of a valid gmail account to be the sender for the digest email, and a recipient to which the email will be sent. 

## Installation/dependencies

Depencies are all listed in `requirements.txt`. I used a virtualenv but you can use whatever works for you. This project was deployed on AWS Lambda, but you can run it from cron as well with a venv.

See https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html for instructions on how to deploy to Lambda.
