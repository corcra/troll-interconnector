from database import *
import tweepy
from settings import *
import urllib3
urllib3.disable_warnings()

#disable warnings in case somebody (like me) is running 
#a Python version < 2.7.9


def TweepyAuth(consumer_key, consumer_secret):
    #only has to be run once, then you can just put the token in secret_data
    
    t_auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth_url = t_auth.get_authorization_url()
    print 'Please authorize: ' + auth_url
    verifier = raw_input('PIN: ').strip()
    t_auth.get_access_token(verifier)
    print t_auth

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)
user = api.me()
print user.name