import sys
import json

raw_data = sys.stdin.readlines()[0]
raw_data = '[' + raw_data.replace('}', '},')[:-1] + ']'
tweets = json.loads(raw_data);
dedup = {}
for tweet in tweets:
    dedup[tweet['id']] = tweet

print json.dumps(dedup)
