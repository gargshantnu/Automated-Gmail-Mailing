import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMail(receivers):
    fromaddr = "myMail"
    passw = "myPass"
    myMail = fromaddr

    for toaddr in receivers:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Attendance"

        body = """Python test mail.
        Hii this is Shantnu this mail is send just for testing purpose.
        please make an acknowledgment to me that you have received this email from me"""

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(myMail, passw)

        text = msg.as_string()

        server.sendmail(myMail, toaddr, text)
