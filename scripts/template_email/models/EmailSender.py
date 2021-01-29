import smtplib
import socks
import logging

class EmailSender:
    def __init__(self, sender, user_account, smtp_config, proxy = False, proxy_config = None):
        self.sender = sender
        self.user_account = user_account
        self.smtp_config = smtp_config
        self.proxy = proxy
        self.proxy_config = proxy_config
        self.setup_smtp()
        
    
    def setup_smtp(self):
        if self.proxy:
            socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, self.proxy_config['server'], self.proxy_config['port'])
            socks.wrap_module(smtplib)
        try:
            self.smtp = smtplib.SMTP(self.smtp_config['server'], self.smtp_config['port'])
            self.smtp.ehlo()
            self.smtp.starttls()
            self.smtp.login(self.user_account['username'], self.user_account['password'])
        except Exception as e:
            logging.error("Create mail object failed! Reason:{}".format(e))
            raise e


    def send(self, receiver, mail):
        try:
            logging.info("Start sending email...")
            self.smtp.sendmail(self.sender, receiver, mail.as_string())
            logging.info("Send email to {} successfully!".format(receiver))
        except Exception as e:
            logging.error("Send email to {} failed! Reason:{}".format(receiver, e))
    
    def __del__(self):
        self.smtp.close()