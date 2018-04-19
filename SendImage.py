import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_mail(img_file_name, to):
    img_file_name = os.getcwd() + img_file_name
    img_data = open(img_file_name, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'kajay5080@gmail.com'
    msg['To'] = to

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(img_file_name))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(msg['From'], '--------password-------')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

