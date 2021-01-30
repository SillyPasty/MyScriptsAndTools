import logging
from models.EmailGenerator import EmailGenerator
from models.EmailSender import EmailSender
from models import util
import time

if __name__ == '__main__':
    CFG_PATH = r'scripts\template_email\data\cfg.yaml' # 'scripts\template_email\data_example\cfg.yaml'
    util.init_log()
    logging.info('Start sending.')
    cfg = util.read_cfg(CFG_PATH)
    receivers, infillings = util.get_receivers(cfg['receivers'])
    attachments = util.get_attachment(cfg['attachments'])
    email_sender = EmailSender(cfg['user'], cfg['smtp'], True, cfg['proxy'])
    eg = EmailGenerator(cfg['user'])
    for receiver, infilling in zip(receivers, infillings):
        mail = eg.generate(cfg['email_t'], receiver, infilling, attachments)
        email_sender.send(receiver, mail)
        time.sleep(1)
    logging.info('Sending done.')