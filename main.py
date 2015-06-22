import tweepy
import json
import signal
import sys
import threading

consumer_key = ""
consumer_secret = "";

access_token = "";
access_token_secret = "";

def get_file_for_identifier(identifier, permissions):
    return open(identifier + '_config', permissions)

def write_to_config(identifier, text):
    target = get_file_for_identifier(identifier, 'w')
    target.write(text)
    target.close()

def validate_since_id(id):
    return id if not id else '0'

def read_config(identifier):
    f = get_file_for_identifier(identifier, 'r')
    since_id = validate_since_id(f.read())
    f.close()
    return since_id

def get_since_id(identifier):
    return read_config(identifier)

class TweetHandler:
    def __init__(self, identifier):
        self.identifier = identifier

    def to_ascii(self, tweet):
        return tweet.text.encode('ascii', errors='ignore')

    def update_config_file(self, tweet):
        write_to_config(self.identifier, str(tweet.id))

    def to_json_string(self, tweet):
        return json.dumps({
            'text': self.to_ascii(tweet),
            'id': str(tweet.id),
            'created_at': str(tweet.created_at)
        })

    def append_to_output(self, tweet):
        with open(self.identifier + '_out', 'a') as out:
            out.write(self.to_json_string(tweet))

    def handle(self, tweet):
        self.append_to_output(tweet)
        self.update_config_file(tweet)

def stream(api, query, identifier):
    is_complete = False
    while not is_complete:
        try:
            cursor = tweepy.Cursor(
                api.search,
                q=query,
                since_id=get_since_id(identifier),
                since="2015-06-10",
                until="2015-06-17",
                lang="en")
            handler = TweetHandler(identifier)
            for tweet in cursor.items():
                handler.handle(tweet)
            is_complete = True
        except Exception:
            is_complete = False


def signal_handler(signal, frame):
    sys.exit(0)

def get_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    return api

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    api = get_api();
    nba = '#NBAFinals2015'
    warriors = '#Warriors'
    t1 = threading.Thread(target=stream, args = (api, nba + ' ' + warriors, 'nba_and_warriors'))
    t2 = threading.Thread(target=stream, args = (api, nba + ' -' + warriors, 'nba_only'))
    t3 = threading.Thread(target=stream, args = (api, warriors + ' -' + nba, 'warriors_only'))
    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
