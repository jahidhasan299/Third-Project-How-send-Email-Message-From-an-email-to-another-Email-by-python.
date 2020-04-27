import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'From Who & Where came it'
email['to'] = 'Receiver@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'
email.set_content(html.substitute({'name': 'Jack'}),'html ')
with smtp.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender@gmail.com', 'password')
    smtp.send_message(email)
    print(" Email successfully sent")