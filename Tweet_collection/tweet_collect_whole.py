from twitterPredictor.Hello_world_tweepy import *

def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        """
        On crée les path jusqu'aux fichiers contenant les keywords et les hashtags
        On les ouvre et on en extrait les informations utiles pour pouvoir ouvrir un search API
        """
        file_keywords = file_path + '.keywords_candidate_' + str(num_candidate) + '.txt'
        file_hashtags = file_path + '.hashtags_candidate_' + str(num_candidate) + '.txt'
        keywords = []
        hashtags = []
        with open(file_keywords, 'r') as file:
            lines = file.readlines()
            for line in lines:
                split_line = line.split(", ")
                keywords += split_line
        with open(file_hashtags,'r') as file:
            lines = file.readlines()
            for line in lines:
                split_line = line.split(", ")
                hashtags += split_line
        return keywords + hashtags
    except IOError:
        print("Cannot open")
        return []

def get_tweets_from_candidates_search_queries(queries, twitter_api):
    # on définit une connexion à l'API
    connexion = twitter_api
    # pour chaque mot clé, on effectue une recherche de tweet
    for word in queries:
        tweets = connexion.search(word,rpp=100)
        for tweet in tweets:
            print(tweet.text)



#print(get_tweets_from_candidates_search_queries(['Donald Trump'], twitter_setup()))
