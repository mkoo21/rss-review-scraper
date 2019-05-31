from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL = 'REDACTED'
PASS = 'REDACTED'

RECIPIENT = 'koo.martin@gmail.com'

"""
msg.attach(MIMEText("The secret password is 42.", 'plain'))
s.send_message(msg)
s.quit()
"""


def send_mail(html_msg):
    s = SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(EMAIL, PASS)

    msg = MIMEMultipart('alternative')
    msg['FROM'] = EMAIL
    msg['TO'] = RECIPIENT
    msg['SUBJECT'] = "Hello from Python!"
    msg.attach(MIMEText(html_msg, 'html'))
    s.send_message(msg)
    s.quit()
