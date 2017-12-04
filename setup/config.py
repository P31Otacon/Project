# authorize access 
import tweepy
from tweepy import OAuthHandler

consumer_key = ' '
consumer_secret = ' '
access_token = ' '
access_secret = ' '

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# store tweepy authentication into a variable
api = tweepy.API(auth)
