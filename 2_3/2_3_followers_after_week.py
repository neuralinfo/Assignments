#Kasane Utsumi - 3/14/2015
#2_3_followers_after_week.py
#This code iterates through first 10 users in db_followers and retrieves followers for the same users after a week, then stores the result in the db_followers_after_week collection. Please see documentation for more elaboration. 
 
import os 
import json
import pymongo
from bson.json_util import dumps
import tweepy
import time
import signal

def interrupt(signum, frame):
   print "Interrupted, closing ..."
   exit(1)

#twitter setup
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth=None
api=None

try: 
   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   auth.set_access_token(access_token, access_token_secret)
   api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
except:
   print "twitter setup failed"
   exit()

#mongo setup
try:
   mongoConnection = pymongo.MongoClient()
except:
   print "Connection failed"
   exit()

#get tables
db_followers= mongoConnection['twitter_analyzer'].db_followers

if db_followers == "None":
   print "db_followers not found"
   exit()

db_followers_after_week = mongoConnection['twitter_analyzer'].db_followers_after_week

#empty old value from the table
db_followers_after_week.drop()

#to get top 10
index = 0

for user in  db_followers.find(timeout=False):
   followerList = [] 

   #only look for follower ids for user I have to put into db_followers since i had to run this program few times because of network issue
   if db_followers_after_week.find({'id' : user["id"]}).count() == 0:
      uid = user["id"]
      print "userId" +  str(uid) +  " count of followers from twitter call 1 week ago: " + str(len(user["followerIds"]))

      for page in tweepy.Cursor(api.followers_ids,user_id=uid).pages():
	 
         followerList.extend(page)
         time.sleep(60)
   
      #see if number of followers match with number of ids retrieved. This is just a sanity check, since number of followers
      #could have changed from the time tweet was collected
      print "count of followers from twitter call made now:" + str(len(followerList))
  
      followerOfUser = {"id": uid, "followerIds" : followerList}
      db_followers_after_week.insert(followerOfUser)

      index +=1
      if index == 10:
         break

