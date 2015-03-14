#!/usr/bin/env python
#
# David Paculdo
# W205
# Assignment 3

import sys
import nltk
import re
import string


# positive and negative words from: http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html
pos_words=[word.strip() for word in open("positive-words.txt").readlines()]
neg_words=[word.strip() for word in open("negative-words.txt").readlines()]

my_file=open("most_retweeted.txt")
sentiment_file=open("sentiment_analysis.txt","w")

from_string=""

# reading re-tweet file to clean up, tokenize and classify each tweet
for tweet in my_file:
	tweet=tweet[3:]
	tweet=tweet.translate(None,"/:#.,-'?")
	
	sentence=""
	pos_count=0
	neg_count=0
	for word in tweet.strip().split(" "):
		if not word.startswith("http") and not word.startswith("@"):
			sentence=sentence+word.lower()+" "
		
	tokens=nltk.word_tokenize(sentence)
	for token in tokens:
		if token in pos_words:
			pos_count+=1
		if token in neg_words:
			neg_count+=1
	sentiment_total=pos_count-neg_count
	
	sentiment_file.write("Sentiment Analysis: "+str(sentiment_total)+"\tOriginal Tweet: "+tweet)
