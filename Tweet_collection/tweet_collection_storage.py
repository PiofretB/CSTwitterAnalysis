import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from twitter_collect.twitter_connection_setup import *

def store_tweets(tweets,filename):
    # I open a file with writing access
    with open(filename, 'w') as f:
        for tweet in tweets:
            # Every tweet is added to the file
            json.dump(tweet._json, f, indent=4)

#store_tweets(collect(), "tweets.json")

with open('tweet.json', 'r') as file:
    data = json.load(file)

df = pd.Series(data)

df.to_frame()
print(df)
