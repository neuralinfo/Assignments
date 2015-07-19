
import os
import sys
import json
import nltk
import csv
from nltk.corpus import stopwords
sys.path.append('C:\Python27\Lib\site-packages')

os.system(u'aws s3 sync s3://berkeley-w205-spooner-emr-output/assign2 s3')

import json
import nltk
import os
import csv
from nltk.corpus import stopwords

os.system(u'aws s3 sync s3://berkeley-w205-spooner-emr-output/assign2 s3')

import tweepy
consumer_key = "aIm94IFtW1Q7AssW8zFdvtOn2";
consumer_secret = "PYh7dVt9Kec69bHKvT8vaSEOyUY6EYYvSaAJhXBGIqc0s70HQ8";
access_token = "3219874850-Zex9ksNc4yKnK5NYFvH6NsOuXVTHWoha40AbL8F";
access_token_secret = "MHAujfOvfjYmosILChlqb4uYUrMCjPkruOvhl6pQf6L0b";
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

import pymongo

try:
    conn=pymongo.MongoClient()
    print "Connected!"
except pymongo.errors.ConnectionFailure, e:
   print "Connection failed : %s" % e

db_restT = conn[u'db_restT']
db_tweets = conn[u'db_tweets']

#1.1 and 1.2
originals = db_restT[u'originals']
if 'originals' in db_restT.collection_names():
    originals.remove()
originalsB = db_tweets[u'originalsB']
if 'originalsB' in db_tweets.collection_names():
    originalsB.remove()

path = "C:\Users\Benjamin\Documents\Assignments_Berkeley\W205\Assignment3\s3"
for file_n in os.listdir(path):
    if file_n[:6] == "tweets" and file_n[-4:] == "json":
        f = open(path+"/"+file_n)
        json_block = json.load(f)
        for each in json_block:
            a = {"id": str(each['id']), "rtweet_count": each['retweet_count'], "user_name": each['user']['name'], "user_location": each['user']['location']} 
            originalsB.insert(a)
            b = {"id": str(each['id']), "user_name": each['user']['name'], "text": each['text']}
            originals.insert(b)

#2.1
top_rtweets = db_tweets[u'top_rtweets']
if 'top_rtweets' in db_tweets.collection_names():
    top_rtweets.remove()
answer_f = open("2_1_asnwer.txt","w+")
for doc in originalsB.find().sort('rtweet_count', -1).limit(30):
    top_rtweets.insert(doc)
    #print doc
    answer_f.write(str(doc)+'\n')
answer_f.close()

#2.2
#set up collection
lex_diversity = db_restT[u'lex_diversity']
if 'lex_diversity' in db_restT.collection_names():
    lex_diversity.remove()

#extract text for each user
cleaned_words = []
for user in originals.find().distinct("user_name"):
    user_text = ''
    for record in originals.find({"user_name": user}):
        user_text = user_text + ' ' + record['text']
    tokens = nltk.tokenize.word_tokenize(user_text)
    for word in tokens:
        if not word in stopwords.words('english'):
            cleaned_words.append(word)
    cleaned_words = [w.lower() for w in cleaned_words]
    lex_div = float(len(set(cleaned_words)))/len(cleaned_words)
    #print lex_div
    #print user
    a = {"user_name": user, "lexical_diversity":lex_div}
    lex_diversity.insert(a)
    cleaned_words=[]
    
#find top 30 most diverse users
#write to text file
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.style.use('ggplot')
from pandas import DataFrame
answer_f = open("2_2_asnwer.txt","w+")
for each in lex_diversity.find().sort('lexical_diversity', -1).limit(30):
    #print each
    answer_f.write(str(each)+'\n')
answer_f.close()

df = pd.DataFrame(list(lex_diversity.find().sort('lexical_diversity', -1).limit(30)))
df.plot(kind='bar', x='user_name', y='lexical_diversity', style='o')

#2.3
top_rtweets = db_tweets[u'top_rtweets']
db_followers = conn[u'db_followers']
followers_pre = db_followers[u'followers_pre']
if 'followers_pre' in db_followers.collection_names():
    followers_pre.remove()
#followers_post = db_followers[u'followers_post']
#if 'followers_post' in db_followers.collection_names():
#    followers_post.remove()
followers_stopped = db_followers[u'followers_stopped']
if 'followers_stopped' in db_followers.collection_names():
    followers_stopped.remove()
    
for user in top_rtweets.find().distinct("user_name"):
    try:
        for item in tweepy.Cursor(api.followers_ids, screen_name=user).items(30):
            a={"user":user,"follower":item}
            followers_pre.insert(a)
            #followers_post.insert(a)
    except:
        a={"user":user,"follower":"None"}
        followers_pre.insert(a)
        #followers_post.insert(a)

for user in followers_pre.find().distinct("user"):
    for pre in followers_pre.find({'user':user}):
        post_list = []
        for each in followers_post.find({'user':user}):
            post_list.append(each['follower'])
        #print post_list
        if pre['follower'] not in post_list:
            followers_stopped.insert(pre)

db_followers = conn[u'db_followers']
followers_pre = db_followers[u'followers_pre']
followers_post = db_followers[u'followers_post']
followers_stopped = db_followers[u'followers_stopped']

answer_f=open('2_3_asnwer.txt', 'w+')
for each in followers_stopped.find():
    #print each
    answer_f.write(str(each)+'\n')
answer_f.close()