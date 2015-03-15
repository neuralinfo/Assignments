import json
import boto
from boto.s3.key import Key
import signal
import sys
import os

def interrupt(signum, frame):
   print "Interrupted, closing ..."
   exit(1)

signal.signal(signal.SIGINT, interrupt)

class TweetSerializer:
   out = None
   first = True
   tweetCount = 0
   maxCount = 0
   fileCount = 0
   bucket = None
   fileName = None
   folderName = "tweetsTest"
   tweetTextOnly = False 

   def __init__(self, maxCount=10,bucket=None, folderName="tweetsTest", tweetTextOnly = False ):
      self.maxCount = maxCount
      self.bucket = bucket
      self.folderName = folderName
      self.tweetTextOnly = tweetTextOnly

   def start(self):
      self.fileCount += 1
      self.fileName = "tweets-" +str(self.fileCount)+".json"
      fname= self.folderName + "/"+ self.fileName
      
      try:
        self.out = open(fname,"w+")
      except:
        print "opening file failed for " + fname
        exit()

      self.out.write("[\n")
      self.first = True

   def end(self):
      if self.out is not None:
         if not self.tweetTextOnly: #ending char required only for json tweet        
            self.out.write("\n]\n")
         self.out.close()
         key = Key(self.bucket)
         key.key=os.path.join(self.folderName, self.fileName)
         try:
            key.set_contents_from_filename(self.folderName + "/"+self.fileName)
         except:
            print "Storing to amazon failed for:" + self.fileName
            
      self.out = None
      os.remove(self.folderName + "/"+ self.fileName)
 

   def write(self,tweet):
      if self.tweetCount == 0:
         self.start() #initialize
      if not self.first: #write delimiter if not the first item in the file

         if self.tweetTextOnly: #for tweet only, just put line break. For tweet json, put comma
            self.out.write("\n")
         else: 
            self.out.write(",\n")

      self.first = False
      
      if self.tweetTextOnly: #for tweet only
         self.out.write(tweet)
      else:
         self.out.write(str(tweet))

      self.tweetCount += 1

      if self.tweetCount == self.maxCount:
         self.end()
         self.tweetCount = 0


