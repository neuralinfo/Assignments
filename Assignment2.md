# Mining Social Media Data #

Twitter is commonly used for sentiment analysis. However, the first task is to  gather and store the data about the topic of interest before examining the sentiment. The purpose of this assignment is to provide an opportunity for you to work on gathering and storing the twitter data.


## Data Acquisition Task ##

In this task, you will gather the data for these hashtags: #NBAFinals2015 and #Warriors.
As part of this task, you need to:

1. Write an acquisition program to pull the tweets for each hashtag and the tweets that have both of the hashtags simultaneously with in a week.  You also need to chunk your data (using your design decisions) and give yourself the ability to re-run the process reliable in case of failures (Resiliency).
2. Organize the resulting raw data into a set of tweets and store these tweets into S3.
3. Analyze the acquired tweets by producing a histogram (a graph) of the words.

 
## What to Turn In ##
 
1. A link to your S3 bucket documented in your README.md file.  Make sure to make it publicly accessible.

2. Your twitter acquisition code.

3. The histogram.
