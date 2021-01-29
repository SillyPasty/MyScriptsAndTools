import logging
from models.EmailGenerator import EmailGenerator
from models.EmailSender import EmailSender

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

SENDER = 'yubowang2020@gmail.com'
SMTP_CONFIG = {'server': 'smtp.gmail.com', 'port': 587}
PROXY_CONFIG = {'server': '127.0.0.1', 'port': 10808}
USER_ACCOUNT = {'username':'my mail', 'password':'mypsd'}
SUBJECT = "Test Test"
RECEIVER = "wangyb0327@gmail.com"

if __name__ == '__main__':
    receiver = RECEIVER
    email_sender = EmailSender(SENDER, USER_ACCOUNT, SMTP_CONFIG, True, PROXY_CONFIG)
    infilling = {'test':'This is the infill test text.'}
    attachment = [r'scripts\template_email\data\testpdf.pdf']
    eg = EmailGenerator(SENDER)
    mail = eg.generate(r'scripts\template_email\templates\test.html', receiver, infilling, attachment)
    email_sender.send(receiver, mail)