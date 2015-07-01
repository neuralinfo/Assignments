# Storing, Retrieving, and Analyzing Social Media Data Using MongoDB#




##  Background Info ##
This assignment is built on top of the previous assignment.

We'd like to utilize the twitter data (raw formats) that you gathered in assignment 2. 

##Lexical diversity  ##
Lexical diversity is a measurement that provides a quantitative measure for the diversity of an individual's or group's vocabulary.  It is calculated by  finding the number of unique tokens in the text divided by the total number of tokens in the text. 

##Tasks  ##

Note: When you start working on the data acquistion parts, make sure you look at part 2.3 which also requires data pulls and plan accordingly.

## 1-Storing Tasks ##


  1.1- Write a python program to automatically retrieve and store the JSON files (associated with the tweets that include  #NBAFinals2015 hashtag and the tweets that include #Warriors hashtag) 
     returned by the twitter REST api in a MongoDB database called db_restT. 
     
  1.2- Write a python program to insert the chucked tweets associated with the #NBAFinals2015 hashtag and the tweets  associated with the #Warriors hashtag  that you have gathered in the assignment 2 and stored on S3 to a MongoDB database called db_tweets. This program should pull the inputs automatically from your S3 buckets holding the chuncked tweets and insert them into the db_tweets.

## 2-Retrieving and Analyzing Tasks ##
  2.1- Analyze the tweets stored in db_tweets by finding the top 30 retweets as well as their associated usernames (users authored them) and the locations 
   of users.
   
  2.2- Compute the lexical diversity of the texts of the tweets for each of the users in db_restT and store the results back to Mongodb. To compute the lexical diversity of a user, you need to find all the tweets of a particular user (a user's tweets corpus), find the number of unique words in the user's tweets corpus, and divide that number by the total number of words in the user's tweets corpus. 
  
  You need to create a collection 
    with appropriate structure for storing the results of your analysis.
    
  2.3- Write a python program to create a db called db_followers that stores all the followers for all the users that
     you find in task 2.1. Then, write a program to find the un-followed friends after a week for the top 10 users( users that have the highest number of followers in  task 2.1)
     since the time that you extracted the tweets. In other words, you need to look for the people following the top 10 users at time X (the time that you extracted the tweets) and then look at the people following the same top 10 users at a later time Y (one-week after X) to see who stopped following the top 10 users.
     
  2.4- .(Bonus task) Write a python program and use NLTK to analyze the top 30 retweets of task 2.1 as positive or negative (sentiment analysis). This is the bonus part of the assignment.

##3-Storing and Retrieving Task##

  3.1- Write a python program to create and store the backups of both db_tweets and db_restT to S3. It also should have a capability of
     loading the backups if necessary.
     

## What to Turn In ##
 
1. A link to your S3 bucket that holds the backups documented in your README.md file.  Make sure to make it publicly accessible.

2. Your python codes.

3. The plot of your lexical diversities in task 2.2 showing the lexical diveristies of the top 30 users and the result of the sentiment analysis in task 2.4 if you complete the bonus part.
