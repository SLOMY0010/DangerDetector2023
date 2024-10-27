import smtplib
import ssl
import pickle

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_mail(img, dangers):
    
    # Emails imformation
    # Get the password of the sender email you would like to use by using the apppassowrds feature in your google account.
    # For information on how to use this feature, watch the first section of this youtube video: https://www.youtube.com/watch?v=g_j6ILT-X0k
    email_sender = ""
    email_reciever = "" 

    email_password = "" # 16 character apppassword

    # Email's components
    subject = "Warning!"
    body = "Dangers:\n"

    dangers = "\n".join(dangers)
    body = body + dangers

    # Server's information
    context = ssl.create_default_context()
    port = 587
    server = "smtp.gmail.com"

    # Forming the Email
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_reciever
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Include the attachment and send the email
    filename = img
    print(filename)
    with open(filename, 'rb') as attachement:

        # Encode the file
        attachement_package = MIMEBase('application', 'octet-stream')
        attachement_package.set_payload((attachement).read(), 'jpg')
        encoders.encode_base64(attachement_package)
        attachement_package.add_header('Content-Disposition', 'attachment', filename=filename)

        # Attach the file to the message
        msg.attach(attachement_package)

        text = msg.as_string()

        with smtplib.SMTP(server, port) as smtp:
            smtp.starttls(context=context)
            smtp.login(email_sender, email_password)
            print("Connected to the server")
            smtp.sendmail(email_sender, email_reciever, text)
            print('Email was sent succesfully')
