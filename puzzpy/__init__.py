import os
import re


def root_path():
    return os.path.dirname(__file__)


def file_cleanup(fname):
    return fname.replace(' ', '_').lower()


def phrase_cleanup(phrase):
    return re.sub(r'[^a-z ]', '', phrase.lower().strip())
