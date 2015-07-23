
=============

**
In this assignment, you implement map-reduce jobs for various tasks:

#**Tasks**

**Data collection:** 
 
 Write an acquisition program that can acquire the tweets between June 6th and July 5th of 2015 for the official FIFA Women World Cup hashtag (“#FIFAWWC”), as well as team code hashtags (e.g. “#USA” and “#GER”) and store them with appropriate structures in *WC2015.csv* on S3. You can find more information about teams [here](http://www.fifa.com/womensworldcup/teams/) and the hashtags [here](https://twitter.com/fifawwc). *WC2015.csv* will be used in the following tasks.
 
There is no hard requirement for the amount of tweets that you should gather. However, you should gather reasonable amount of tweets to be able to perform the analysis part. Note that you need to gather the historical data for which you need to design a strategy and use techniques such as web scrapping for the specified time frame (June 6th and July 5th of 2015).

#**Analysis Programs**

 In this part, you will write map-reduce programs to analyze the tweets stored in *WC2015.csv*
 
 1. Write a map-reduce program that counts the number of words with more than 10000 occurrences.
 2. Write a map-reduce program to compute the tweet volume on an hourly basis (i.e., number of tweets per hour) .  A sample output is like:

| Date     | Hour | Number of tweets   |
| :------- | ----: | :---: |
| 8/15 | 00|  1763    |
| 8/15     | 01   |   5432   |
| 8/15     | 02    |  3279  |

 3  -Write a map-reduce program to compute the top 20 URLs tweeted by the users
 
 4  -Write a map-reduce program that for each word in the tweets' text,  computes the occurrences of other words appear in every tweet that it appeared.
For example, assume that we have the following text as a tweet text.

> I have seen USA match today. I am so happy that they won :)

*With the word I,*

• have occurs once.

• seen occurs once.

• and so on.

*With the word have,*

• I occurs twice.

Here are an example of sample outputs:

– USA occurs 10000 times with Canada

– Germany occurs 500 with England


 

5- (bonus) Modifying the program in 4, write a map-reduce program to compute [pointwise mutual information](http://en.wikipedia.org/wiki/Pointwise_mutual_information), which is a function of two events x and y:

  ![](http://www.sciweavers.org/download/Tex2Img_1437692896.jpg)
  
  The larger the  PMI for x and y is, the more information can be gathered about the probability of seeing y having just seen x. Your program should compute the PMI of words  that appear together more than 50 times or more among entities in *WC2015.csv*. To be more specific,  you need to find pairs of words that co-occur in 50 or more tweets. 



**Questions:** 

Using/modifying the above programs, answer the following questions:

 1. What is the average length of tweets (in number of characters) in *WC2015.csv*?
 2. Draw a table with all the team support hashtags you can find and the number of support messages. What country did get apparently the most support?
 3. How many times the word *USA* occur with the word *Japan*?
 4. How many times the word *champion* occur with the word *USA*?


> **Note:**

> -  Convert every string into lower-case.
> -  Only consider english tweets
> -  For simplicity, get rid of all punctuation, i.e., any character other than a to z and space. 
> - The output of mapper and reducer is part of your design decisions. However, you should be able to answer the above questions.
> - Use EMR for running your map-reduce tasks and include the configuration of your cluster in the architecture design document.



#**Twitter Archive Search**

You will use the *whoosh* API to index the tweets in the dataset to answer some standard queries as described bellow.

###**Task**

 - Write a python program that uses whoosh to index the archive (*WC2015.csv*) based on various fields. The fields are part of your design decisions.
 - Write a python program that takes queries (you need to design the supported queries)  and search through the indexed archive using *whoosh.* A sample query to the program can be: *RT:yes, keywords* returns all the retweets  that are related to the keywords. Your program should handle at least 4 queries ( of your choice) similar to the sample query.



#**Deliverables**

 1. A link to your collected tweets and the index directory created by whoosh on S3
 2. Your source codes. Make sure you follow the assignment submission guidelines 
 2. You should  answer to each of the questions in the architecture design file. You also need to explain how you used map-reduce to obtain the data you needed in each case as well as how the overall index/search structure is designed and describe the supported keyword search queries.
