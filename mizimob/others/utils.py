import re
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def validate_email(email):
    regex = re.compile(r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,'
                       r'3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
    return re.match(regex, email)


def validate_phone(number):
    regex = re.compile(r'^[+]*[(]?[0-9]{1,4}[)]?[-\s\./0-9]*$', re.IGNORECASE)
    final = re.match(regex, number)
    return final


def send_email(_to, subject, body) -> bool:
    _from = "admin@fuprox.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = _from
    message["To"] = _to

    # Turn these into plain/html MIMEText objects
    part = MIMEText(body, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part)
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("mail.fuprox.com", 465, context=context) as server:
        server.login(_from, "Japanitoes")
        if server.sendmail(_from, _to, message.as_string()):
            return True
        else:
            return False