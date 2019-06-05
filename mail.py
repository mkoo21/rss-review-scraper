from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

EMAIL = 'SENDER_EMAIL_HERE'
PASS = 'SENDER_PASSWORD_HERE'
RECIPIENT = 'RECIPIENT_EMAIL_HERE'


def send_mail(html_msg):
    s = SMTP(host='smtp.gmail.com', port=587)
    #s = SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(EMAIL, PASS)

    msg = MIMEMultipart('alternative')
    msg['FROM'] = EMAIL
    msg['TO'] = RECIPIENT
    msg['SUBJECT'] = "Bleep, bloop, here are the reviews I found that were published on {}".format(datetime.today().date())
    msg.attach(MIMEText(html_msg, 'html'))
    s.send_message(msg)
    s.quit()
