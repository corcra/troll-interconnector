#!/bin/python
# One script to rule them and in the darkness troll them.

import madbot
import tweepy
import tweet_scraper
from credz import consumer_key, consumer_secret, access_token, access_token_secret

# --- get set up with the twitters --- #
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# example from the tweepy page!
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text

# --- STUFF --- #
selector = '#hashtag'

# --- option one: find target, then find match --- #
# identify target to neutralise
target = madbot.get_target(selector)
# find a partner for them
match = madbot.get_match(target, selector)

# --- option two: find many targets, pair them off --- #
# find many potential targets
targets = madbot.find_trolls(selector)
# pair them off
target, match = madbot.pair_trolls(targets)

# --- now manage the mischief --- #
tweet = madbot.form_connection(target, match, selector)
# ... and then you send the tweet, somehow (API-implementation specific)
#


