#Kasane Utsumi 
import os 
import json
import pymongo
from bson.json_util import dumps

try:
   mongoConnection = pymongo.MongoClient()
except:
   print "Connection failed"
   exit()

#get tables
db_streamT = mongoConnection['twitter_analyzer'].db_streamT
db_retweets = mongoConnection['twitter_analyzer'].db_all_retweets
db_top30RetweetedUsers = mongoConnection['twitter_analyzer'].db_top30_users

db_retweets.drop()
db_top30RetweetedUsers.drop()

#create a dictionary of retweeted id is key, and number of occurrence as a value 
retweetDict = dict()

#also, dump all of the tweets into db_all_retweets so it would be easy to get user and location for top 30 later. 

for tJson in db_streamT.find():
   tweetJson = json.loads(dumps(tJson['tweetJson'])) 
   if 'retweeted_status' in tweetJson: 
      retweet = tweetJson['retweeted_status'] 
      id = retweet['id'] 
      retweetDBEntry = {"id" : id, "retweetJson" : retweet} 
      db_retweets.insert(retweetDBEntry) 
      if id in retweetDict: 
         retweetDict[id] += 1 
      else: retweetDict[id] = 1 


#check the dictionary to make sure it has what I want 
#for key in retweetDict: 
   #if (retweetDict[key] >1): 
      #print str(key) + " " + str(retweetDict[key]) 

#convert retweetDict into tuples so I can sort by number of frequencies, then sort by frequncy 
retweetTuple = sorted(tuple(retweetDict.iteritems()),key=lambda x: (-x[1],x[0]))

#check the tuple to see if it has what I want
#for (id,frequency) in retweetTuple:
   #if frequency > 1:
      #print str(id) + " " +str(frequency)

#print out the top tweeted user , also store them in top30_users collection so they can be retreived for other analysis
tupleIndex = 0
for (id,frequency) in retweetTuple:
   retweet = db_retweets.find_one({"id":id})
   
   if (retweet == None):
      print "Something went wrong, could not find retweet with id" + str(id)
   else:
      retweetJson = json.loads(dumps(retweet["retweetJson"]))
      topTweetedUser = retweetJson['user']

      userDBEntry = {"id": topTweetedUser['id'], "userInfo" : topTweetedUser}
      db_top30RetweetedUsers.insert(userDBEntry)
 
      #print out retweet, user name and location
      print "Top Retweet Rank " + str(tupleIndex+1) 
      print "Tweet: " + retweetJson["text"]
      print "User: " + topTweetedUser["name"] + " at " + topTweetedUser['location']
      print " "
 
      #get only top 30
      tupleIndex = tupleIndex + 1   
      if tupleIndex == 30:
         exit()
