from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import logging
import os
from bs4 import BeautifulSoup

class EmailGenerator:
    def __init__(self, sender):
        self.sender = sender
    
    def generate(self, template_path, receiver, infilling, attachments):
        subject, text = self.__parse_template(template_path, infilling)
        email = MIMEMultipart('mixed')
        email['Subject'] = subject
        email['From'] = self.sender
        email['To'] = receiver
        email.attach(MIMEText(text, 'plain', 'utf-8'))
        # Add attachment
        for attachment in attachments:
            try:
                _, filename = os.path.split(attachment)
                sendpart = MIMEApplication(open(attachment, 'rb').read())
                sendpart.add_header('Content-Disposition', 'attachment', filename=filename)
                email.attach(sendpart)
            except Exception as e:
                logging.error("Attach file {} failed. Reason: {}".format(attachment, e))

        return email

    
    def __parse_template(self, template_path, infilling):
        try:
            with open(template_path, 'r') as f:
                soup = BeautifulSoup(f, features="html.parser")
                subject = soup.head.text

                for k, v in infilling.items():
                    tag = soup.select('#' + k)[0]
                    tag.string = v

                text = soup.body.get_text()
                return subject, text
        except Exception as e:
            logging.error("Parse_template failed!, Reason{}".format(e))
            raise e


