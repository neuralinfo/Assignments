#! /usr/bin/env python
#
# David Paculdo
# W205
# Assignment 3

import sys
import pymongo
import tweepy
import signal
import json
import os
import string
import time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = os.environ.get("twitter_consumer_key");
csecret = os.environ.get("twitter_consumer_secret");

atoken = os.environ.get("twitter_access_token");
asecret = os.environ.get("twitter_access_token_secret");


# Defaults for Twitter Stream
try:
	termList=str(sys.argv[1]) #term list must be in quotes on command line e.g. "#microsoft,#mojang"
	print "Search terms: "+termList
except:
	print "Usage: Assignment3_1_1.py \"[search terms separated by comma]\""


# DB name for mongodb
db_name="db_streamT"

# Instance of the Twitter stream listener
class listener(StreamListener):
    def __init__(self, api):
        self.api = api
        super(StreamListener, self).__init__()

        #change name of client and database to what we want it to be
        self.db = pymongo.MongoClient()
        self.db = self.db[db_name]

    def on_data(self, data):
        data = json.loads(data)
        #data=data.encode("utf-8")

        text=filter(lambda x: x in string.printable, data['text'])
        print text

        # Writing to mongodb. Can change tweets collection to something else
        self.db.tweets.insert(data)

        return True

    def on_error(self, status):
        print >> sys.stderr, 'Encountered error with status code:', status
        if status==420:
            time.sleep(600)
        return True

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True


#Begin Twitter stream access
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api=tweepy.API(auth, retry_count=5, retry_delay=5, retry_errors=set([401,404,500,503]),timeout=120)


try:
    twitterStream = Stream(auth, listener(api))
    twitterStream.filter(track=[termList])
except KeyboardInterrupt:
    print("Interrupt called")
    sys.exit()
