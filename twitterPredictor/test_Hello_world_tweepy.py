from twitterPredictor.Hello_world_tweepy import *

# on vérifie que la fonction ne renvoie pas un objet nul
def test_twitter_setup():
    assert twitter_setup() != None
