import smtplib
import socks
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import COMMASPACE
import EmailSender
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

SENDER = 'yubowang2020@gmail.com'
SMTP_CONFIG = {'server': 'smtp.gmail.com', 'port': 587}
PROXY_CONFIG = {'server': '127.0.0.1', 'port': 10808}
USER_ACCOUNT = {'username':'yubowang2020@gmail.com', 'password':'lele0327'}
SUBJECT = "Test Test"

def send_mail(receivers, text, sender=SENDER, user_account=USER_ACCOUNT, subject=SUBJECT):
    msg_root = MIMEMultipart()  # 创建一个带附件的实例
    msg_root['Subject'] = subject  # 邮件主题
    msg_root['To'] = receivers  # 接收者
    msg_text = MIMEText(text, 'html', 'utf-8')  # 邮件正文
    msg_root.attach(msg_text)  # attach邮件正文内容

    email_sender = EmailSender.EmailSender(SENDER, USER_ACCOUNT, SMTP_CONFIG, True, PROXY_CONFIG)
    email_sender.send(receivers, msg_root)

if __name__=="__main__":
    send_mail('wangyb0327@gmail.com', "<h1>IMPORTANT!</h1><p>Test Test1</p>")