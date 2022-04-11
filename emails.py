import smtplib
import os
from email.message import EmailMessage

Email_Address = os.environ.get('EMAIL_USER')
Email_Password = os.environ.get('EMAIL_PASSWORD')
file1 = 'File Path'
file2 = 'File Path'
msg = EmailMessage()
msg['Subject'] = 'Testing'
msg['From'] = 'From Address'
msg['To'] = 'To Address'
msg.set_content('This is a test.')

for file in file1:
    with open(file1, 'rb') as f:
        _fileData = f.read()
        _fileName1 = f.name

for file in file2:
    with open(file2, 'rb') as f:
        _fileData = f.read()
        _fileName2 = f.name

    msg.add_attachment(_fileData, maintype = 'application', subtype = 'octet-strem', filename = _fileName1)
    msg.add_attachment(_fileData, maintype = 'application', subtype = 'octet-strem', filename = _fileName2)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('EMAIL_USER', 'EMAIL_PASSWORD')
    smtp.send_message(msg)