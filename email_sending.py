import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import hashlib
import os



def password_encryption(password):
    hash_func = hashlib.sha1()
    encode_string = password.encode()
    hash_func.update(encode_string)
    mes = hash_func.digest()
    return mes


sender = input("Enter mail:")
security = input("Enter password:")
receiver = input("Enter mail:")
password = "something"
pas = password_encryption(password)

body = '''Hello,This is your pdf and following is your password {} and following is your encrypted password {}'''.format(password, pas)
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'This email has an attacment, a pdf file'
message.attach(MIMEText(body, 'plain'))
files = os.listdir("C:/Users/avina/OneDrive/Desktop/Training/27_apr_22/Pdf Encryption_27_Apr_22/pdf/")
for x in files:
        pdfname = '{}'.format("C:/Users/avina/OneDrive/Desktop/Training/27_apr_22/Pdf Encryption_27_Apr_22/pdf/"+x)
        binary_pdf = open(pdfname, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binary_pdf).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender, security)
        text = message.as_string()
session.sendmail(sender, receiver, text)
session.quit()
print("Mail Sent")
