import sys
import json
import operator
import re

lines = sys.stdin.readlines()
hist = {}
pattern = re.compile('[\W\d]')

for line in lines:
  tweets = json.loads(line)
  for id, tweet in tweets.iteritems():
    for word in tweet['text'].split():
      tokens = re.sub(pattern, ' ', word)
      for token in tokens.split():
        term = token.lower()
        if not term in hist:
          hist[term] = 1
        else:
          hist[term] = hist[term] + 1

sorted_hist = sorted(hist.items(), key=lambda x:x[1])
for pair in sorted_hist:
  print str(pair[1]) + ' ' + pair[0]
