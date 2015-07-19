import os
import sys
import pymongo
from bson import BSON, decode_all

try:
    conn=pymongo.MongoClient()
    print "Connected!"
except pymongo.errors.ConnectionFailure, e:
   print "Connection failed : %s" % e

db_restT = conn[u'db_restT']
db_tweets = conn[u'db_tweets']

#backup
for coll in db_restT.collection_names():
    c = db_restT[coll]
    with open(coll+'.bson', 'wb+') as f:
        for each in c.find():
            f.write(BSON.encode(each))
for coll in db_tweets.collection_names():
    c = db_tweets[coll]
    with open(coll+'.bson', 'wb+') as f:
        for each in c.find():
            f.write(BSON.encode(each))

db_restT_list = ['originals','lex_diversity']
db_tweets_list = ['originalsB','top_rtweets']
for each in db_restT_list:
    target = db_restT[each]
    if each in db_restT.collection_names():
        target.remove()  
    with open(each+'.bson', 'rb') as f:
        target.insert(decode_all(f.read()))