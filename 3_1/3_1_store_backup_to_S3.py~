#Kasane Utsumi - 3/14/2015
#3_1_store_backup_to_S3.py
#This code make a backup of db_tweets and db_streamT and uploads to corresponding location on S3. The items in db_streamT are bundled into 500 per json file(value), and for db_tweets 1500 per csv file(value)

import signal
import pymongo
import TweetSerializer
import boto
from boto.s3.connection import S3Connection
from bson.json_util import dumps
import csv
from boto.s3.key import Key
import os

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
db_tweets = mongoConnection['twitter_analyzer'].db_tweets
db_streamT = mongoConnection['twitter_analyzer'].db_streamT

if db_tweets == None or db_streamT == None:
   print "either collection does not exist!"
   exit()


aws_access_key_id =''
aws_secret_access_key= ''
aws_bucket_name='
conn = None
bucket = None


try:
   conn = S3Connection(aws_access_key_id,aws_secret_access_key)
   bucket = conn.get_bucket(aws_bucket_name)
except:
   print "S3 connection failed or bucket connection failed"
   exit()

#store json from db_streamT first

#chunk into 500 tweet json per file
tweetSerializerJson = TweetSerializer.TweetSerializer(500,bucket,"db_streamT", False)

for tweetJson in db_streamT.find():
   tweetSerializerJson.write(dumps(tweetJson))
tweetSerializerJson.end()

print "finished uploading json tweets, now try just tweets"

#now store tweets only

#utility function to open file, write content of tweet array and upload to S3 bucket
def writeCSVAndUploadTweetOnly(tweetDirectory,tweetFilePrefix,fileNumber,arrayOfTweets):
   fileName = tweetFilePrefix + str(fileNumber) + ".csv"

   with open(tweetDirectory + "/" + fileName, "w+") as output:

      writer = csv.writer(output, lineterminator='\n')

      for i in range(len(arrayOfTweets)):
         t = arrayOfTweets[i]
         #if tweet text contains carriage return, must warp by " so that it doesn't get split into multiple tweets while restoring the db from s3. 
         if ('\r' in t or '\n' in t):             
            arrayOfTweets[i]  = '"' + t + '"'
            #writer.writerows(t)   

      writer.writerow(arrayOfTweets)
      
   key = Key(bucket)
   key.key=os.path.join(tweetDirectory, fileName)
   try:
      key.set_contents_from_filename(tweetDirectory + "/"+fileName)
   except:
      print "Storing to amazon failed for:" + fileName   
   os.remove(tweetDirectory + "/"+ fileName)


# number of tweet text to store per file
tweetCountPerFile = 1500
tweetDirectory = "db_tweets"
tweetFilePrefix = "tweetOnly"
fileNumber = 1

#keep tweets in array, and once reached 1500, dump into csv. It is not a most elegant way to do this
#but I am running out of time... 
tweetList = []

for tweetText in db_tweets.find():

   tweetList.append(tweetText['text'].encode('utf8'))
    
   if len(tweetList) == tweetCountPerFile:
      
      writeCSVAndUploadTweetOnly(tweetDirectory,tweetFilePrefix,fileNumber,tweetList)
      #reinitialize array
      tweetList = []
      fileNumber +=1 
   
#serialize leftover tweets
if len(tweetList) != 0:
   writeCSVAndUploadTweetOnly(tweetDirectory,tweetFilePrefix,fileNumber,tweetList)



   

