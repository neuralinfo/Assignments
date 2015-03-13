#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# David Paculdo
# W205
# Assignment 3

import os
import pymongo
import string
from collections import Counter


#Global program variables
db_name="db_tweets"
db_name2="db_restT"
db_name3="db_followers"

coll="tweets"
users="userlist"
conn=pymongo.MongoClient()


#Make sure database and collection are accessible:
try:
	db=conn[db_name]
	collection=db[coll]
	
	db2=conn[db_name2]
	collection2=db2[coll]

	db3=conn[db_name3]
	collection3=db3[users]
except:
	print "dbname or collection does not exist"
	sys.exit()


#Create empty list and file to write most common re-tweets
my_file=open("most_retweeted.txt","w")
tweet_list=[]
prev_tweet=""

#Search for retweets
for tweets in collection.find():
	text=filter(lambda x: x in string.printable, tweets['tweet'])
	text=text.replace("\n","")
	
	if text.startswith("RT "):
		tweet_list.append(text)

#Count and sort retweet list to find the 30 most common retweets.
tweet_count=Counter(tweet_list)
tweet_most=tweet_count.most_common(30)


#Block to find information on the users who retweeted the 30 most common retweets
#Then insert into mongodb
for tweet,count in tweet_most:
	for tweets in collection2.find():
		text=filter(lambda x: x in string.printable, tweets['text'])
		text=text.replace("\n","")
		
		if tweet==text:
			userinfo=tweets['user']	
			screen_name=userinfo['screen_name']
			followers_count=userinfo['followers_count']
			uid=userinfo['id']
			location=userinfo['location']
			
			if text!=prev_tweet:
				print text
				my_file.write(text+"\n")
				prev_tweet=text
			collection3.insert({"username":screen_name.encode("utf-8"), "user_id":uid, "follower_count":followers_count, "location":location.encode("utf-8")})
