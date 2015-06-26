# Assignment 2 by Benjamin Spooner #

## Comments ##

1. search.py connects to twitter API and chunks the data
2. index_file.txt stores name of files based on search string and stores their total number of lines for that search. This is used to index the analysis code.
3. upload.py uploads chunks to S3 and then analyses them using nltk to produce the histogram graphs
4. upload.py eliminates stopwords but retains punctuation. With internet lingo often even single character punctuation can be as meaningful as words

## S3 Bucket ##
1.https://console.aws.amazon.com/s3/home?region=us-west-2#&bucket=berkeley-w205-spooner-emr-output&prefix=assign2/
