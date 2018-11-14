from twitterPredictor.Hello_world_tweepy import *

def collect():
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)

print(collect())
