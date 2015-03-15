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
from bson.json_util import loads


try:
   mongoConnection = pymongo.MongoClient()
except:
   print "Connection failed"
   exit()
#get tables
db_streamT = mongoConnection['twitter_analyzer'].db_streamT

#extract tweet from tweet json 
for tJson in db_streamT.find():
   print json.loads(dumps(tJson['tweetJson']))["text"].encode('utf8')
   #print json.loads(dumps(tJson['tweetJson']))
   exit() 


