from twitterPredictor.Hello_world_tweepy import *

def collect():
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)

#print(collect())

def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 20)
    for status in statuses:
        print(status.text)
    return statuses

#print(collect_by_user(1976143068)) #Emmanuel Macron


from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True




def collect_by_streaming(recherche):

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=[recherche])

print(collect_by_streaming('Donald Trump'))
