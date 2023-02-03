#email_graphic.py
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
def send_image(username,password,to_address,from_address,
               message,preamble,file_path):
    msg = MIMEMultipart()
    msg["Subject"] = message
    msg["From"] = from_address
    msg["To"] = to_address
    msg.preamble = preamble
    file = file_path
    fp = open(file,"rb")
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.send_message(msg)
    server.quit()
