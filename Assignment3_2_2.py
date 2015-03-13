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

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from nltk.tokenize import RegexpTokenizer

#Defining the tokenizer
#used to clean up the tweets a little bit
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')

#Variables for mongodb
db_name="db_streamT"
coll1="tweets"
coll2="word_db"
coll3="lexical_db"


#Connecting to mongodb and make sure collections are accessible
conn=pymongo.MongoClient()
try:
	db=conn[db_name]
	collection=db[coll1]
except:
	print "dbname or collection does not exist"
	sys.exit()

#Variables for lexical diversity
total_words=0
word_count={}


#Block to determine the lexical diversity of the tweets
for data in collection.find():
	
	#cleans up any non-printable characters
	text=filter(lambda x: x in string.printable, data['text'])
	text=text.replace("\n","")
	text=string.lower(text)
	
	tokens=tokenizer.tokenize(text)
	total_words += len(tokens)
	for word in tokens:
		if word in word_count:
			word_count[word]+=1
		else:
			word_count[word]=1


#Calculation of the lexical diversity
unique_words=len(set(word_count))
lexical_diversity=float(unique_words)/total_words

#Writes lexical diversity to file
my_file=open("lexical_diversity.txt","w")
my_file.write("total number of words: %i\n" %(total_words))
my_file.write("total number of unique words: %i\n" %(unique_words))
my_file.write("lexical diversity of corpus: %f\n" %(lexical_diversity))


#Insert words and number of times the word occurred into mongodb
words=db[coll2]
for key, value in word_count.iteritems():
	words.insert({"word":key, "count":value})


#Insert lexical diversity numbers into mongodb
lexical=db[coll3]
lexical.insert({"total_words":total_words, "unique_words":unique_words, "lexical_diversity":lexical_diversity})
