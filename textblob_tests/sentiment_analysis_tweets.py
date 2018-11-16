from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from twitter_collect.twitter_connection_setup import *
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

#les tweets regroupent ceux mentionnant une personne
def tweets_sentiment_analysis(name):
    connexion=twitter_setup()
    tweets = connexion.search(name, count = 50)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    tweets_list = data['tweet_textual_content'].values
    polarity = []
    subjectivity = []
    for tweet in tweets_list:
        #print(tweet)
        Analysis=TextBlob(tweet).sentiment
        polarity += [Analysis[0]]
        subjectivity += [Analysis[1]]
    print('For '+name+', we get :')
    print('Average polarity : ' + str(np.average(polarity)))
    print('Average subjectivity : '+ str(np.average(subjectivity)))


print(tweets_sentiment_analysis('@realDonaldTrump'))
print(tweets_sentiment_analysis('@BarackObama'))

connexion = twitter_setup()
# on crée des listes vides qui vont contenir les différents tweets en fonction de leur analyse par TextBlob
pos_tweets = []
neu_tweets = []
neg_tweets = []
tweets = connexion.search('@realDonaldTrump', count = 100)
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
tweets_list = data['tweet_textual_content'].values
for tweet in tweets_list:
    analysis = TextBlob(tweet).sentiment
    # Si la polarité est >0 : le tweet est positif
    if analysis[0]>0:
        pos_tweets.append(tweet)
    # si la polarité est <0 : le tweet est négatif
    elif analysis[0]<0:
        neg_tweets.append(tweet)
    # sinon, le tweet est neutre
    else:
        neu_tweets.append(tweet)


print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))

