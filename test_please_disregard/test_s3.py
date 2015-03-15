import os
import sys
import tweepy
import datetime
#mport urllib
import signal
import json
import boto
from boto.s3.connection import S3Connection
#import tweetserializer
#import tweetanalyzer
from boto.s3.key import Key
#import numpy as np
#import pylab as pl
import pymongo



aws_access_key_id =''
aws_secret_access_key= ''
aws_bucket_name=''


s3conn = S3Connection(aws_access_key_id,aws_secret_access_key)

print "conn good"
bucket = s3conn.get_bucket(aws_bucket_name)


