# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

class TweepError(Exception):
    """Tweepy exception"""

    def __init__(self, reason, response=None):
        self.reason = reason  #self.reason = unicode(reason) in python 2
        self.response = response
        Exception.__init__(self, reason)

    def __str__(self):
        return self.reason

