#Kasane Utsumi - 3/14/2015
#3_1_restore_backup_from_S3.py
#This code restores backup files made from db_tweets and db_streamT and restores the data into db_tweetsRestored and db_streamTRestored collections. 

import json 
import os
import boto
from boto.s3.key import Key
import string
import signal
import os
import pymongo
from boto.s3.connection import S3Connection
from bson.json_util import dumps
import yaml
import csv

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
db_tweetsRestored = mongoConnection['twitter_analyzer'].db_tweetsRestored
db_streamTRestored = mongoConnection['twitter_analyzer'].db_streamTRestored

db_tweetsRestored.drop()
db_streamTRestored.drop()

aws_access_key_id =''
aws_secret_access_key= ''
aws_bucket_name=''

conn = None
bucket = None


try:
   conn = S3Connection(aws_access_key_id,aws_secret_access_key)
   bucket = conn.get_bucket(aws_bucket_name)
except:
   print "S3 connection failed or bucket connection failed"
   exit()

#get file from s3 and store locally and store into db_streamTRestored

for key in bucket.list("db_streamT"):

   if key.name.endswith('/'): 
      continue
   key.get_contents_to_filename(key.name)

   filer = open(os.getcwd() + "/" + key.name,"r")

   #use yaml to get result as str type and not unicode type
   data =  yaml.load(filer.read())

   filer.close()
   #file was read into memory, now delete it to save disk space
   os.remove(os.getcwd()  + "/" + key.name)
   for jsonTweet in data:
      del jsonTweet["_id"]
      db_streamTRestored.insert(jsonTweet)

#get file from s3 and store locally and store into db_tweetsRestored
for key in bucket.list("db_tweets"):

   if key.name.endswith('/'): 
      continue
   key.get_contents_to_filename(key.name)

   #read from csv file, dump each text into db_tweetsRestored
   with open(os.getcwd() +"/"+ key.name,'r') as csvfile:
      csvreader = csv.reader(csvfile)

      for row in csvreader:
         for col in row:
            db_tweetsRestored.insert({"text" : col.decode('utf8')})
  
   os.remove(os.getcwd() +"/"+ key.name)

	

