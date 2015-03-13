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


#Variables for twitter accessibility
ckey = os.environ.get("twitter_consumer_key");
csecret = os.environ.get("twitter_consumer_secret");

atoken = os.environ.get("twitter_access_token");
asecret = os.environ.get("twitter_access_token_secret");


#Variables for mongo DB and collections
db_name="db_followers"
coll1="followers"
coll2="unfollowers"


#Attempt to connect to DB and collection to make sure they are accessible
conn=pymongo.MongoClient()
try:
	db=conn[db_name]
	collection=db[coll1]
	collection2=db[coll2]
except:
	print "dbname or collection does not exist"
	sys.exit()


followed=[]


#Access mongodb to find the top followed users and their number of followers
for userid in collection.find():
	uid=userid['user_id']
	screen_name=userid['screen_name']
	follower_list=userid["follower_list"]
	follower_num=len(follower_list)
	
	followed.append([uid,follower_num,follower_list,screen_name])


#Sort list from most followed to least followed
#Then take the top 10 from the list
followed_sorted=sorted(followed, key=lambda x:x[1], reverse=True)
top_followed=followed_sorted[:10]

top_followed_id=[[item[0],item[2],item[3]] for item in top_followed]
#print top_followed


#Connection to Twitter
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


#Get new list of Twitter followers
#Compare against old list of Twitter followers
#Insert those who unfollowed into mongo
new_followed=[]
for ids in top_followed_id:
	top_id=ids[0]
	old_follower_list=ids[1]
	screen_name=ids[2]
	
	new_follower_list=[]	
	for page in tweepy.Cursor(api.followers_ids,id=top_id).pages():
		#print page
		new_follower_list.extend(page)
		print "RESTING\n"
		time.sleep(60)	
		
	follower_count=len(new_follower_list)
	new_followed.append([top_id,follower_list])
	
	print str(top_id)+"\t\tnew follower count:"+str(follower_count)
	
	#Compare the new list and the old list to see who is not in the new list
	follower_set = set(new_follower_list)
	unfollowed = [x for x in old_follower_list if x not in follower_set]

	unf_list=[]

	#print screen_name+" unfollowed by:\t"

	if len(unfollowed)>0:
		try:
			users=api.lookup_users(user_ids=unfollowed)
			for u in users:
				unf_screen_name=u.screen_name
				print "\t"+unf_screen_name
				unf_list.append(unf_screen_name)
		except:
			#Just in case there are no valid IDs to return
			print "\tNothing to return. All IDs are invalid"
			
	else:
		#In case no one unfollowed them
		print "\tNo one unfollowed them!"

	#print "Unfollowed list: "
	#print unf_list
	
	#Insert into mongo the IDs of those who unfollowed someone
	collection2.insert({"screen_name":screen_name,"user_id":top_id,"unfollowed_by":unf_list})