import sys
import tweepy
import datetime
import urllib
import signal
import json
import signal
import time
import gc
import os

# Don't forget to install tweepy
# pip install tweepy

consumer_key = "key"
consumer_secret = "secret"
access_token = "key"
access_token_secret = "secret"

stop = 0

def interrupt(signum, frame):
   print "Interrupted, closing ..."
   stop = 1

signal.signal(signal.SIGINT, interrupt)

class TweetSerializer:
   out = None
   first = True
   count = 0
   def start(self, chunk):
      fname = "tweets-"+chunk+str(self.count)+".json"
      self.out = open(fname,"w")
      self.out.write("[\n")
      self.first = True

   def end(self):
      if self.out is not None:
         self.out.write("\n]\n")
         self.out.close()
      self.out = None

   def write(self,tweet):
      if not self.first:
         self.out.write(",\n")
      self.first = False
      self.out.write(json.dumps(tweet._json).encode('utf8'))
      self.count += 1


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

q1 = urllib.quote_plus("#NBAFinals2015 -#Warriors")  # URL encoded query
q2 = urllib.quote_plus("#Warriors -#NBAFinals2015")
q3 = urllib.quote_plus("#Warriors #NBAFinals2015")

ser1 = TweetSerializer()
ser2 = TweetSerializer()
ser3 = TweetSerializer()
index_file = open('index_file.txt',"w+")

print "Starting query 1\n"
c = tweepy.Cursor(api.search, q1, since="2015-06-07", until="2015-06-014", lang="en", monitor_rate_limit=True).items()
index = None
while True:
    stop = 0
    if ser1.count%1000 == 0:
        ser1.end()
        ser1.start(q1)
        gc.collect()
    print "debug 1 "+str(ser1.count)
    try:
        tweet=c.next()
        index = tweet.id
        ser1.write(tweet)
    except tweepy.TweepError as e:
        print e.reason
        time.sleep(900)
        c = tweepy.Cursor(api.search, q1, since="2015-06-07", until="2015-06-014", since_id=index,lang="en", monitor_rate_limit=True).items()
        continue
    except StopIteration as I:
        break
    if stop == 1:
        break
  #print tweet._json
ser1.end()
index_file.write('tweet'+q1+' '+str(ser1.count)+"\n")

print "Starting query 2\n"
c = tweepy.Cursor(api.search, q2, since="2015-06-07", until="2015-06-014", lang="en", monitor_rate_limit=True).items()
while True:
    if ser2.count%1000 == 0:
        ser2.end()
        ser2.start(q2)
        gc.collect()
    print "debug 2 "+str(ser2.count)
    try:
        tweet=c.next()
        index = tweet.id
        ser2.write(tweet)
    except tweepy.TweepError as e:
        print e.reason
        time.sleep(900)
        c = tweepy.Cursor(api.search, q2, since="2015-06-07", until="2015-06-014", since_id=index,lang="en", monitor_rate_limit=True).items()
        continue
    except StopIteration as I:
        break
    if stop == 1:
        break
   #print tweet._json
ser2.end()
index_file.write('tweet'+q2+' '+str(ser2.count)+"\n")

print "Starting query 3\n"
c = tweepy.Cursor(api.search, q3, since="2015-06-07", until="2015-06-014", since_id=index, lang="en", monitor_rate_limit=True).items()
while True:
   if ser3.count%1000 == 0:
      ser3.end()
      ser3.start(q3)
      gc.collect()
   print "debug 3 "+str(ser3.count)
   try:
      tweet=c.next()
      index = tweet.id
      ser3.write(tweet)
   except tweepy.TweepError as e:
      print e.reason
      time.sleep(900)
      c = tweepy.Cursor(api.search, q3, since="2015-06-07", until="2015-06-014", since_id=index,lang="en", monitor_rate_limit=True).items()
      continue
   except StopIteration as I:
      break
   if stop == 1:
      break
   #print tweet._json
ser3.end()
index_file.write('tweet'+q3+' '+str(ser3.count)+"\n")

print "Program complete\n"