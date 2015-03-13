#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# David Paculdo
# W205
# Assignment 3

from boto.s3.connection import S3Connection
from boto.s3.key import Key
import os
import pymongo


#Amazon AWS variables
AWS_KEY=os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET=os.environ.get("AWS_SECRET_KEY")


#Connection to AWS
conn = S3Connection(AWS_KEY, AWS_SECRET)
#bucket must already be created
bucket = conn.get_bucket("w205-assignment-2-dpaculdo")
tmpfile="temp_from_s3"

k=Key(bucket)
k.key="microsoft_OR_mojang_2015-02-07_2015-02-14_tweets_0.txt"

k.get_contents_to_filename(tmpfile)
my_file=open(tmpfile,"r")


#mongodb variables
db_name="db_tweets"
coll="tweets"


#mongodb connection
conn=pymongo.MongoClient()
db=conn[db_name]
collection=db[coll]


#Insert into mongodb. Replace "\n" with space.
for line in my_file:
	collection.insert({"tweet":line.replace("\n"," ")})


#Clean up
os.remove(tmpfile)
