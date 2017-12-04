import tweepy 
import json


# Twitter API credentials
consumer_key = ' '
consumer_secret = ' '
access_key = ' '
access_secret = ' '


def get_all_tweets(screen_name):
        
    # authorize Twitter account and initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    # initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    # save most recent tweets
    alltweets.extend(new_tweets)
    
    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        # save most recent tweets
        alltweets.extend(new_tweets)
        
        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))
       
    # write tweet objects to JSON
    file = open('tweet.json', 'wb') 
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    file.close()

if __name__ == '__main__':
    # pass in the username(s) of the accounts you want to download
    # get_all_tweets accepts only one argument
    get_all_tweets(" ")


