from database import *
import tweepy
from settings import *
import urllib3

#disable warnings in case somebody (like me) is running 
#a Python version < 2.7.9

urllib3.disable_warnings()

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'
    
    