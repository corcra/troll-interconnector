import database.db as db
import database.models as models
import tweepy
from settings import *
import urllib3
urllib3.disable_warnings()

#disable warnings in case somebody (like me) is running 
#a Python version < 2.7.9


# inheriting from object is a kludge for 2.x, no longer needed in 3 if we
# migrate to that.
class TweetScraper(object):
    
    def TweepyAuth(self, consumer_key, consumer_secret):
        # only has to be run once then you can just put the token in secret_data
        # would be best be broken out into some sort of utils library later
        t_auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, 
            TWITTER_CONSUMER_SECRET)
        auth_url = t_auth.get_authorization_url()
        print 'Please authorize: ' + auth_url
        verifier = raw_input('PIN: ').strip()
        t_auth.get_access_token(verifier)
        return t_auth


    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)
    
    def search_tweets(self, query):
        """ Will suck down and store results of a search in the db """
        results = self.api.search(q=query, lang="en")
        for result in results:
            print result.id_str
            # now let's break out the bits we're interested in
            # check if the tweet exists
            tweet_result = db.session.query(models.Tweet).filter_by(
                id_str=result.id_str).first()
            if tweet_result:
                # entry already exists, skip it
                continue
            else:
                tweet_author = db.session.query(models.TwitterUser).get(
                    result.user.id)
                if not tweet_author:
                    # new user previously unseen, add to db
                    tweet_author = models.TwitterUser(id=result.user.id, 
                        name=result.user.name)
                    db.session.add(tweet_author)
                tweet_result = models.Tweet(id_str=result.id_str, 
                content=result.text, author=tweet_author)
                print tweet_result.id_str
            db.session.commit()
            
t_scraper = TweetScraper()
t_scraper.search_tweets("mouse")
