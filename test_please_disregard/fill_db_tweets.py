import os
#jjimport sys
#import tweepy
#jimport datetime
#mport urllib
#import signal
import json
#import boto
#from boto.s3.connection import S3Connection
#import tweetserializer
#import tweetanalyzer
#from boto.s3.key import Key
#import numpy as np
#import pylab as pl
import pymongo
from bson.json_util import dumps
try:
   mongoConnection = pymongo.MongoClient()
except:
   print "Connection failed"
   exit()
#get tables
db_streamT = mongoConnection['twitter_analyzer'].db_streamT
db_tweets = mongoConnection['twitter_analyzer'].db_tweets

#extract tweet from tweet json 
for tJson in db_streamT.find():
   tweetOnlyEntry = {"id" : tJson['id'], "text" : json.loads(dumps(tJson['tweetJson']))['text']}
   db_tweets.insert(tweetOnlyEntry)
exit()

