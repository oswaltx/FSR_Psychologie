mails = {"Mail 1": {"Betreff": "Das ist der erste betreff"

}}
print(mails["Mail 1"]["Betreff"])



import imaplib
import email
from email.header import decode_header

# Connect to the IMAP server
imap_server = 'imap.uni-koeln.de'  # Replace with your IMAP server
email_user = ''  # Replace with smail-name
email_pass = ''  # Replace with your password

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_user, email_pass)
status, messages = imap.select("INBOX")
print(status)
#prints number of messages
messages = int(messages[0])
print(messages)
