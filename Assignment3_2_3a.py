#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# David Paculdo
# W205
# Assignment 3

import os
import pymongo
import string
import sys
import tweepy
import time

from tweepy import OAuthHandler


#Twitter access variables
ckey = os.environ.get("twitter_consumer_key");
csecret = os.environ.get("twitter_consumer_secret");

atoken = os.environ.get("twitter_access_token");
asecret = os.environ.get("twitter_access_token_secret");


#Variables for mongodb connection
db_name="db_followers"
coll1="userlist"
coll2="followers"

#Attempt to connect to DB and collections and make sure they are accessible
conn=pymongo.MongoClient()
try:
	db=conn[db_name]
	collection=db[coll1]
	collection2=db[coll2]
except:
	print "dbname or collection does not exist"
	sys.exit()


#Twitter access
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,retry_count=5, retry_delay=5, retry_errors=set([401,404,500,503]),timeout=120)


usercount=1
followed=[]


#Find the user id of the retweeters and find the userids of their followers
for userid in collection.find():
	uid=userid['user_id']
	screen_name=userid['username']

	follower_list=[]
	
	#Find a page of followers at a time and extend list
	for page in tweepy.Cursor(api.followers_ids,id=uid).pages():
		follower_list.extend(page)
		#put in place just to make sure we're not hung up somewhere
		print "RESTING for 60 seconds\n"
		time.sleep(60)	
		
	follower_count=len(follower_list)
	followed.append([screen_name,follower_count])
	
	#Prints out the screen name of the most followed and their number of followers
	print str(usercount)+": "+screen_name+"\t\t"+str(follower_count)
	usercount+=1
	
	#Insert into mongodb the screen name, the user id, and the list of followers
	collection2.insert({"screen_name":screen_name,"user_id":uid,"follower_list":follower_list})

