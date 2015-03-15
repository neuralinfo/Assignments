#Kasane Utsumi - 3/14/2015
#2_2_plot_lexical_diversity.py
#This code generates a histogram which shows frequency of lexical deversity range based on db_lexical_diversity collections. 
import os 
import json
import pymongo
from bson.json_util import dumps
from bson.son import SON
import numpy as np
import pylab as pl
import decimal
import matplotlib.pyplot as plt
import signal

def interrupt(signum, frame):
   print "Interrupted, closing ..."
   exit(1)

try:
   mongoConnection = pymongo.MongoClient()
except:
   print "Connection failed"
   exit()

#get tables
db_lexical_diversity = mongoConnection['twitter_analyzer'].db_lexical_diversity

if db_lexical_diversity == None:
   print "db_lexical_diversity doesn't exist. Exiting.."
   exit()

plotArray = []

for user in db_lexical_diversity.find():
   plotArray.append(user['lexical_diversity'])
#   plotDictionary[float(user['lexical_diversity'])]= user['username']

plt.hist(np.asarray(plotArray, dtype='float'))
plt.show()
 

exit()
 
#X=np.arange(len(plotDictionary))
#pl.bar(X,plotDictionary.keys(),width=0.2)
#pl.xticks(X,plotDictionary.values())
#ymax= max(plotDictionary.keys())+1
#pl.ylim(0,ymax)
#pl.show()


