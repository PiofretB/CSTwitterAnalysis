from Tweet_collection.tweet_collect_whole import *
from twitter_collect.twitter_connection_setup import *
def get_replies_to_candidate(num_candidate):
    connexion = twitter_setup()
    answers = connexion.search(num_candidate, in_reply_to_status_id_str=num_candidate, count = 20)
    for ans in answers:
        print(ans)
    return

print(get_replies_to_candidate(1976143068))

'''def get_retweets_of_candidate(num_candidate):
    connexion = twitter_setup()
    retweets = connexion.retweets(num_candidate,count=20)
    return retweets

print(get_retweets_of_candidate(1976143068))'''
