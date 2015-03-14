# David Paculdo
# W205 - Assignment 3
# Storing, Retrieving, and Analyzing Social Media Data Using MongoDB#



####################
## 1-Storing Task ##
####################

1.1- Write a python program to automatically store the JSON files (associated with the #microsoft and #mojang hash tags) returned by twitter api in  a database called db_streamT.

File: Assignment3_1_1.py
Usage: Assignment3_1_1.py "list of search terms" [including quotes]

This file takes the list of search teams and searches using the Twitter Stream API. All associated data are stored in a DB called db_streamT and in a collection called tweets.


1.2- Write a python program to insert the chucked data tweets (of assignment 2) that you have stored on S3 to mongoDB in a database called db_tweets.

Files: Assignment3_1_2.py and Assignment3_1_2b.py

This program has hard-coded the files necessary to read, as well as the DB name and collection name, and runs without any command-line input. These can be easily changed to accept a command-line input.

There is an additional file titled Assignment3_1_2b.py which loads the data from Assignment 2 and inserts into a database called 'db_restT'. This will be used in Assignment 2.1. There are no command-line inputs.



#####################################
## 2-Retrieving and Analyzing Task ##
#####################################

2.1- Analyze the tweets stored in db_tweets by finding the top 30 retweets as well as their associated usernames and the locations of users.

File: Assignment3_2_1.py

The assumption here is that what is required is the usernames of those who retweeted the top retweets, rather than the usernames of those who originally made the tweet. With that assumption in mind, the program goes through the db_tweets database to find all the retweets and counts those that have been retweeted the most in db_tweets. These are then compared against the tweets in db_restT, and the usernames and locations of those who made the retweets are found from the matching retweets. The results are then placed in a DB called followers.

The text of the top retweets are stored in a file called most-retweeted.txt for ease of use in 2.4.


2.2- Compute the lexical diversity of the tweets stored in db_streamT and store the results back to Mongodb. You need to create a collection with appropriate structure for storing the results of your analysis.

File: Assignment3_2_2.py

The program (again without command-line input) reads the texts of the tweets stored in db_streamT on a tweet-by-tweet basis, and then cleans them up a little bit. The lexical diversity is calculated, then output to a file titled lexical_diversity.txt and a mongo collection called lexical_db in the db_streamT DB.


2.3- Write a python program to create a db called db_followers that stores all the followers for all the users that you find in task 2.1. Then, write a program to find the un-followed friends after a week for the top 10 users( users that have the highest number of followers in  task 2.1) since the time that you extracted the tweets.

Files: Assignment3_2_3a.py and Assignment3_2_3b.py

Assignment3_2_3a.py finds and stores the userids of all of the followers of the retweeters found in 2.1.

Assignment3_2_3b.py finds the ten users with the most followers, and then finds out who unfollowed them.


2.4- (Bonus task) Write a python program and use NLTK to analyze the top 30 retweets of task 2.1 as positive or negative (sentiment analysis). This is the bonus part of the assginmnet.

Files: Assignment3_2_4.py, positive-words.txt, negative-words.txt, most-retweeted.txt.

This program takes a list of positive (positive-words.txt) and negative words (negative-words.txt) and compares them against the top retweets (most-retweeted.txt) from task 2.1 after performing a little bit of cleanup. These are scored as positive or negative and then summed for a total sentiment score, with a more positive score meaning more positive sentiment and a more negative score being more negative sentiment.



###################################
## 3-Storing and Retrieving Task ##
###################################

3.1- Write a python program to create and store the backups of both db_tweets and db_streamT to S3. It also should have a capability of loading the backups if necessary.

File: Assigment3_3_1.py
Usage: Assignment3_3_1.py [backup/restore/list/delete] [database name (not used if first argument is 'list')]
S3 bucket: w205-assignment-3-dpaculdo

This file assumes that the bucket is already created. The file can backup, restore, or a delete a backup of a mongo database. The database files, located in the directory designated by the mongod.conf file, are copied over directly into the S3 bucket. Backups are restored, listed, and deleted from the same bucket, and in the case of restored

