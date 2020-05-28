# --------------------------------------------------------------------------------------------
# Generic python script for sending email over any SMTP host
# Created by: Pooja Bhat
# Date: 26-May-2020
# --------------------------------------------------------------------------------------------

import smtplib, email
from email import encoders
import os
import sys

SMTP_SERVER = 'xxxxx'
SMTP_PORT = 32

# SMTP_USERNAME = ''
# SMTP_PASSWORD = ''

print("To send an attachment execute: `python sendmail.py /path/to/your/attachment`\n\n")

SMTP_FROM = raw_input("Enter FROM address: ")
SMTP_TO = raw_input("Enter TO address: ")
SUBJECT = raw_input("SUBJECT: ")

text=""""""
# MESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT,text)
MESSAGE = '{}\n'.format(text)

msg = email.MIMEMultipart.MIMEMultipart()
body = email.MIMEText.MIMEText(MESSAGE)

if len(sys.argv)==2:
	FILENAME = sys.argv[1]
	if os.path.exists(FILENAME):
		attachment = email.MIMEBase.MIMEBase('text', 'plain')
		attachment.set_payload(open(FILENAME).read())
		attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(FILENAME))
		encoders.encode_base64(attachment)
		msg.attach(attachment)
	else:
		print('The file that you are trying to attach does not exist')
		print('Aborting sendmail')
		sys.exit()

msg.attach(body)
msg.add_header('From', SMTP_FROM)
msg.add_header('To', SMTP_TO)
msg.add_header('Subject', SUBJECT)

# Send message
mailer = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# mailer.connect()
# mailer.login(SMTP_USERNAME, SMTP_PASSWORD)
mailer.sendmail(SMTP_FROM, [SMTP_TO], msg.as_string())
mailer.close()
print("Message has been sent")
