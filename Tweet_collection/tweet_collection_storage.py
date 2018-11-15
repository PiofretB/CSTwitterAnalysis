import json
from twitter_collect.twitter_connection_setup import *
def store_tweets(tweets,filename):
    with open(filename, 'w') as f:
        for tweet in tweets:
            json.dump(tweet._json, f, indent=4)

#store_tweets(collect(), "tweets.json")
