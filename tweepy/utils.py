# Tweepy
# Copyright 2010 Joshua Roesslein
# Felipe Herranz (felHR85@gmail.com)
# See LICENSE for details.

from datetime import datetime
import time
# htmlentitydefs was renamed as html.entities in python3
try:
    import html.entities as htmlentitydefs
except ImportError:
    try:
        import htmlentitydefs
    except ImportError:
        raise ImportError("Import error. There is no html.entities or htmlentitydefs module")

import re
import locale
from urllib.parse import quote


def parse_datetime(string):
    # Set locale for date parsing
    locale.setlocale(locale.LC_TIME, 'C')

    # We must parse datetime this way to work in python 2.4
    date = datetime(*(time.strptime(string, '%a %b %d %H:%M:%S +0000 %Y')[0:6]))

    # Reset locale back to the default setting
    locale.setlocale(locale.LC_TIME, '')
    return date


def parse_html_value(html):

    return html[html.find('>')+1:html.rfind('<')]


def parse_a_href(atag):

    start = atag.find('"') + 1
    end = atag.find('"', start)
    return atag[start:end]


def parse_search_datetime(string):
    # Set locale for date parsing
    locale.setlocale(locale.LC_TIME, 'C')

    # We must parse datetime this way to work in python 2.4
    date = datetime(*(time.strptime(string, '%a, %d %b %Y %H:%M:%S +0000')[0:6]))

    # Reset locale back to the default setting
    locale.setlocale(locale.LC_TIME, '')
    return date


def unescape_html(text):
    """Created by Fredrik Lundh (http://effbot.org/zone/re-sub.htm#unescape-html)"""
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)


def convert_to_utf8_str(arg):
    # written by Michael Norton (http://docondev.blogspot.com/)
    if isinstance(arg, str):
        arg = arg.encode('utf-8')
    elif not isinstance(arg, str):
        arg = str(arg).encode('utf-8')
    return arg


def convert_to_unicodePoints(arg):  # Python 3 or greater

    if not isinstance(arg,str):
        return str(arg, 'utf-8')


def import_simplejson():
    try:
        import json # Python 2.6+
    except ImportError:
        raise ImportError("Can't load a json library")

    return json

def list_to_csv(item_list):
    if item_list:
        return ','.join([str(i) for i in item_list])

def urlencode_noplus(query):
    return '&'.join(['%s=%s' % (quote(str(k), ''), quote(str(v), '')) \
        for k, v in query.iteritems()])