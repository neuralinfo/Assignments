#Kasane Utsumi 
import os 
import json
import pymongo
from bson.json_util import dumps
import tweepy
import time

#twitter setup
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#mongo setup
try:
   mongoConnection = pymongo.MongoClient()
except:
   print "Connection failed"
   exit()

#get tables
db_top30RetweetedUsers = mongoConnection['twitter_analyzer'].db_top30_users
db_followers = mongoConnection['twitter_analyzer'].db_followers


#create an array of unique users
topRetweetedUserList = dict()

for userJson in db_top30RetweetedUsers.find():

   userId = userJson['id']

   #get followers Count for cross checking
   followersCount = json.loads(dumps(userJson['userInfo']))['followers_count']

   if userId not in topRetweetedUserList:
      topRetweetedUserList[userId]  = followersCount

#check the list to make sure it has what I want 
#for uid in topRetweetedUserList: 
#   print str(uid) + " " + str(topRetweetedUserList[uid])

#for each user, make a twitter followers/id call to get list of his/her followers' ids and store it in the db_followers
#db_follower will have 30 rows, the format for each row is:
#{"id":user id, followerIds: list of follower's ids}
for uid in topRetweetedUserList:
       if db_followers.find({'id' : uid}).count() != 0:
          print "found"
       else:
          print "not found"


