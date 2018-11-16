import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from twitter_collect.twitter_connection_setup import *

'''def store_tweets(tweets,filename):
    # I open a file with writing access

    with open(filename, 'w') as f:
        for tweet in tweets:
            # Every tweet is added to a list that will then be added to the Json file

        json.dump(tweet._json, f, indent=4)

#store_tweets(collect(), "tweets.json")

with open('tweet.json', 'r') as file:
    data = json.load(file)
'''

def collect_to_pandas_dataframe(keyword):
    connexion = twitter_setup()
    tweets = connexion.search(keyword,language="fr",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data

collect_to_pandas_dataframe("@EmmanuelMacron")

rt_max  = np.max(collect_to_pandas_dataframe("@EmmanuelMacron")['RTs'])
rt  = collect_to_pandas_dataframe("@EmmanuelMacron")[collect_to_pandas_dataframe("@EmmanuelMacron").RTs == rt_max].index[0]

# Max RTs:
print("The tweet with more retweets is: \n{}".format(collect_to_pandas_dataframe("@EmmanuelMacron")['tweet_textual_content'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(collect_to_pandas_dataframe("@EmmanuelMacron")['len'][rt]))

