import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from twitter_collect.twitter_connection_setup import *
'''
def store_tweets(tweets,filename):
    # I open a file with writing access
    list_tweets = []
    with open(filename, 'w') as f:
        for tweet in tweets:
            # Every tweet is added to a list that will then be added to the Json file
            list_tweets.append(tweet._json)

        json.dump(list_tweets, f, indent=4)

#store_tweets(collect(), "tweets.json")

'''


def collect_to_pandas_dataframe(user_id):
    connexion = twitter_setup()
    tweets = connexion.user_timeline(id = user_id, count = 20)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data
'''
data = collect_to_pandas_dataframe(25073877)
print(data)

rt_max  = np.max(data['RTs'])
rt  = data[data.RTs == rt_max].index[0]

# Max RTs:
print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))

tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

#plt.show()

#print(data['Source'])
#print(data.dtypes)


#tret.plot(figsize=(16,4), label="Retweets", legend=True)
plt.show()
print(data['Likes'])
'''
#Comparaison Likes Macron et Trump
data_Trump = collect_to_pandas_dataframe(25073877)
data_Macron = collect_to_pandas_dataframe(1976143068)

tfavTrump = pd.Series(data=data_Trump['Likes'].values, index=data_Trump['Date'])
tfavMacron = pd.Series(data=data_Macron['Likes'].values, index=data_Macron['Date'])
plt.subplot(211)
tfavTrump.plot(figsize=(16,4), label="Likes des tweets de Trump", legend=True)
tfavMacron.plot(figsize=(16,4), label="Likes des tweets de Macron", legend=True)

#Comparaison Retweets Macron et Trump sur leurs 20 derniers tweets
tretTrump = pd.Series(data=data_Trump['RTs'].values, index=data_Trump['Date'])
tretMacron = pd.Series(data=data_Macron['RTs'].values, index=data_Macron['Date'])
plt.subplot(212)
tretTrump.plot(figsize=(16,4), label="Retweets des tweets de Trump", legend=True)
tretMacron.plot(figsize=(16,4), label="Retweets des tweets de Macron", legend=True)
plt.show()
