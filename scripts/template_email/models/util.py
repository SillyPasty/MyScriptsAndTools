import os
import csv
import logging
import yaml


def init_log():
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(filename=r'scripts\template_email\log\my.log',
                        level=logging.DEBUG,
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT)


def read_cfg(filename):
    with open(filename, 'r') as f:
        y = yaml.load(f, Loader=yaml.FullLoader)
    return y


def get_attachment(attach_dir):
    attach_files = os.listdir(attach_dir)
    attach_path = [os.path.join(attach_dir, f) for f in attach_files]
    return attach_path


def get_receivers(receiver_fp):
    receivers = []
    infillings = []
    with open(receiver_fp) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            keys = headers[1:]
            infilling = {}
            receivers.append(row[0])
            for i, key in enumerate(keys):
                infilling[key] = row[i + 1]
            infillings.append(infilling)
    return receivers, infillings
