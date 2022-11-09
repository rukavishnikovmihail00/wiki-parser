import logging
import sys
from argparse import ArgumentParser


def parse():
    parser = ArgumentParser()
    parser.add_argument("-t", "--title", help="page title")
    parser.add_argument("-l", "--lang", help="page language")
    args = vars(parser.parse_args())
    return args


def init_logger():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    logging.getLogger("urllib3").setLevel(logging.INFO)
    logging.getLogger("wikipediaapi").setLevel(logging.WARNING)
    formatter = logging.Formatter("[%(asctime)s | %(levelname)s]: %(message)s")

    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    root_logger.addHandler(ch)
