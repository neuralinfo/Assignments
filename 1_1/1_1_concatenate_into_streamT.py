#Kasane Utsumi - 3/14/2015
#1_1_concatenate_into_streamT.py
#This code dumps all seven collections starting with db_streamT%StartDate% (%StartDate% is a passed command line argument) into db_streamT

import os
import json
import pymongo
import sys
from bson.json_util import dumps

import signal

def interrupt(signum, frame):
   print "Interrupted, closing ..."
   exit(1)

try:
   mongoConnection = pymongo.MongoClient()
except:
   print "Connection failed"
   exit()

#get tables
db_streamT = mongoConnection['twitter_analyzer'].db_streamT

#clear table
db_streamT.drop()

stream1 = mongoConnection['twitter_analyzer']['db_streamT' + sys.argv[1]]
stream2 = mongoConnection['twitter_analyzer']['db_streamT' + sys.argv[2]]
stream3 = mongoConnection['twitter_analyzer']['db_streamT' + sys.argv[3]]
stream4 = mongoConnection['twitter_analyzer']['db_streamT' + sys.argv[4]]
stream5 = mongoConnection['twitter_analyzer']['db_streamT' + sys.argv[5]]
stream6 = mongoConnection['twitter_analyzer']['db_streamT' + sys.argv[6]]
stream7 = mongoConnection['twitter_analyzer']['db_streamT' + sys.argv[7]]

#get total count for all collection so I can compare with count of db_streamT after filling it up so I know that concatenation was successful. 
individualTotal =  stream1.find().count() +  stream2.find().count() + stream3.find().count() + stream4.find().count() + stream5.find().count() + stream6.find().count() + stream7.find().count()


#clear the current content
db_streamT.drop()

def addThisCollection(collection):
    for content in collection.find():
       db_streamT.insert(content)

addThisCollection(stream1)
addThisCollection(stream2)
addThisCollection(stream3)
addThisCollection(stream4)
addThisCollection(stream5)
addThisCollection(stream6)
addThisCollection(stream7)

print "individual total is " + str(individualTotal)
print "StreamT length is " + str(db_streamT.find().count())
print "Number of items match?: " + str(individualTotal == db_streamT.find().count())

