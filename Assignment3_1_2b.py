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
import string
import ast


#Amazon AWS variables and connection
AWS_KEY=os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET=os.environ.get("AWS_SECRET_KEY")

conn = S3Connection(AWS_KEY, AWS_SECRET)
bucket = conn.get_bucket("w205-assignment-2-dpaculdo")

k=Key(bucket)

filecount=0
#hardcoded rawfile to be transferred
rawfile="microsoft_OR_mojang_2015-02-07_2015-02-14_"+str(filecount)+".raw"
k.key=rawfile


#mongodb variables and connection
db_name="db_restT"
coll="tweets"
conn=pymongo.MongoClient()
db=conn[db_name]
collection=db[coll]


#Iterates through all raw Twitter data files from S3 and inserts into mongodb
while k.exists():
	k.get_contents_to_filename(rawfile)
	my_file=open(rawfile,"r")
	
	for line in my_file:
		#print line
		linedict=ast.literal_eval(line)
		collection.insert(linedict)
		
	my_file.close()
	os.remove(rawfile)
	
	filecount+=1
	rawfile="microsoft_OR_mojang_2015-02-07_2015-02-14_"+str(filecount)+".raw"
	k.key=rawfile

