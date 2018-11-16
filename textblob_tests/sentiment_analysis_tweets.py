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


#print(tweets_sentiment_analysis('@realDonaldTrump'))
#print(tweets_sentiment_analysis('@BarackObama'))

connexion = twitter_setup()
# on crée des listes vides qui vont contenir les différents tweets en fonction de leur analyse par TextBlob
pos_tweets = []
neu_tweets = []
neg_tweets = []
tweets_Trump = connexion.search('@realDonaldTrump', count = 100)
data = pd.DataFrame(data=[tweet.text for tweet in tweets_Trump], columns=['tweet_textual_content'])
tweets_list_Trump = data['tweet_textual_content'].values
for tweet in tweets_list_Trump:
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


#print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
#print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
#print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))



import seaborn as sns

sns.set(style="white", color_codes=True)

y = [TextBlob(tweet).sentiment[0] for tweet in tweets_list_Trump]
x = [TextBlob(tweet).sentiment[1] for tweet in tweets_list_Trump]

# Use JointGrid directly to draw a custom plot
grid = sns.JointGrid(x, y, space=0, height=6, ratio=50)
grid.plot_joint(plt.scatter, color="r")
grid.plot_marginals(sns.rugplot, height=1, color="g")
grid.set_axis_labels(xlabel = 'Subjectivity', ylabel='Polarity')

tweets_Obama = connexion.search('@BarackObama', count = 100)
data = pd.DataFrame(data=[tweet.text for tweet in tweets_Obama], columns=['tweet_textual_content'])
tweets_list_Obama = data['tweet_textual_content'].values

y = [TextBlob(tweet).sentiment[0] for tweet in tweets_list_Obama]
x = [TextBlob(tweet).sentiment[1] for tweet in tweets_list_Obama]

# Use JointGrid directly to draw a custom plot
grid = sns.JointGrid(x, y, space=0, height=6, ratio=50)
grid.plot_joint(plt.scatter, color="b")
grid.plot_marginals(sns.rugplot, height=1, color="m")
grid.set_axis_labels(xlabel = 'Subjectivity', ylabel='Polarity')
plt.title('Opinions sur @BarackObama et @realDonaldTrump')
plt.xlim(0,1)
plt.ylim(-1,1)

plt.show()
