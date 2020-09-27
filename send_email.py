from email.mime.text import MIMEText
import smtplib 
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(RECIPIENT, height, av_height, count):
    # Replace sender@example.com with your "From" address. 
    # This address must be verified.
    SENDER = 'xxxxxx'  
    SENDERNAME = 'xxxxx'
    USERNAME_SMTP = "xxxxxxxx"
    PASSWORD_SMTP = "xxxxxxxx"
    HOST = "xxxxxxxx"
    PORT = 587
    SUBJECT = 'Height data'

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES Test\r\n"
                "This email was sent through the Amazon SES SMTP "
                "Interface using the Python smtplib package."
                )

    # The HTML body of the email.
    BODY_HTML = "Hey there, your height is <strong>%s</strong>. Average Height of all is %s. Total Count is %s."  % (height, av_height, count)

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
    msg['To'] = RECIPIENT
    # Comment or delete the next line if you are not using a configuration set
    

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(BODY_TEXT, 'plain')
    part2 = MIMEText(BODY_HTML, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Try to send the message.
    try:  
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        #stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
    # Display an error message if something goes wrong.
    except Exception as e:
        print ("Error: ", e)
    else:
        print ("Email sent!")
    












