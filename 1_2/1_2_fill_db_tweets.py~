#Kasane Utsumi - 3/14/2015
#1_2_fill_db_tweets.py
#This file takes all tweets (with entire tweet information in json format) from db_streamT and stores tweet text ONLY into db_tweets collection.

import os
import json
import pymongo
from bson.json_util import dumps
import signal

def interrupt(signum, frame):
   print "Interrupted, closing ..."
   exit(1)

signal.signal(signal.SIGINT, interrupt)

try:
   mongoConnection = pymongo.MongoClient()
except:
   print "Connection failed"
   exit()

#get tables
db_streamT = mongoConnection['twitter_analyzer'].db_streamT

if db_streamT == None
   print "db_streamT not found! exiting..." 
   exit()

db_tweets = mongoConnection['twitter_analyzer'].db_tweets

#clear the current content
db_tweets.drop()

#extract tweet from tweet json 
for tJson in db_streamT.find():
   #print json.loads(dumps(tJson["text"])).encode('utf8')
   tweetOnlyEntry = {"text" : json.loads(dumps(tJson["text"]))}
   db_tweets.insert(tweetOnlyEntry)

#check that addition happened fine
print "Does length of db_streamT equal that of db_tweets?" + str(db_streamT.find().count() == db_tweets.find().count())
