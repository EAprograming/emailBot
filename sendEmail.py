import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendemail(email, password, send_to_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    # You now need to convert the MIMEMultipart object to a string to send
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    print('sent email')
    server.quit()
