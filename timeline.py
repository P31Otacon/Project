import tweepy
import json
from tweepy import OAuthHandler

consumer_key = ' '
consumer_secret = ' '
access_token = ' '
access_secret = ' '

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def store(tweet):
    print(json.dumps(tweet))

file = open('timeline.json', 'wb')
for status in tweepy.Cursor(api.home_timeline).items(5000):
    # Process a single status
    json.dump(status._json, file, sort_keys=True)
file.close()

