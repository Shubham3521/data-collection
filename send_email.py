from email.mime.text import MIMEText
import smtplib

def send_email(email, height, av_height, count):
    from_email="shubham3521@gmail.com"
    from_password="Shubham.Gupta13"
    to_email=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>. Average Height of all is %s. Total Count is %s."  % (height, av_height, count) 

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)