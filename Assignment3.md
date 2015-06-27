# Storing, Retrieving, and Analyzing Social Media Data Using MongoDB#




##  Background Info ##
This assignment is built on top of the previous assignment.

We'd like to utilize the twitter data (raw formats) that you gathered in assignment 2. 

##Lexical diversity  ##
Lexical diversity is a measurement that provides a quantitative measure for the diversity of an individual's or group's vocabulary.  It is calculated by  finding the number of unique tokens in the text divided by the total number of tokens in the text. 

Note: When you start working on the data acquistion parts, make sure you look at part 2.3 which also requires data pulls and plan accordingly.

## 1-Storing Task ##


  1.1- Write a python program to automatically retrieve and store the JSON files (associated with the #NBAFinals2015 or #Warriors hash tags) 
     returned by twitter REST api in a MongoDB database called db_streamT. 
     
  1.2- Write a python program to insert the chucked data tweets (of assignment 2) that you have stored on S3 to mongoDB 
     in a MongoDB database called db_tweets.

## 2-Retrieving and Analyzing Task ##
  2.1- Analyze the tweets stored in db_tweets by finding the top 30 retweets as well as their associated usernames (users authored them) and the locations 
   of users.
   
  2.2- Compute the lexical diversity of the texts of the tweets stored in db_streamT and store the results back to Mongodb. You need to create a collection 
    with appropriate structure for storing the results of your analysis.
    
  2.3- Write a python program to create a db called db_followers that stores all the followers for all the users that
     you find in task 2.1. Then, write a program to find the un-followed friends after a week for the top 10 users( users that have the highest number of followers in  task 2.1)
     since the time that you extracted the tweets. In other words, you need to look for the people following the top 10 users at time X (the time that you extracted the tweets) and then look at the people following the same top 10 users at a later time Y (one-week after X) to see who stopped following the top 10 users.
     
  2.4- .(Bonus task) Write a python program and use NLTK to analyze the top 30 retweets of task 2.1 as positive or negative (sentiment analysis). This is the bonus part of the assignment.

##3-Storing and Retrieving Task##

  3.1- Write a python program to create and store the backups of both db_tweets and db_streamT to S3. It also should have a capability of
     loading the backups if necessary.
     

## What to Turn In ##
 
1. A link to your S3 bucket that holds the backups documented in your README.md file.  Make sure to make it publicly accessible.

2. Your python codes.

3. The plot of your lexical diversity in task 2.2 and the result of the sentiment analysis in task 2.4 if you complete the bonus part.
