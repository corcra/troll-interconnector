import database.db as db
import database.models as models
import tweepy
from settings import *
import urllib3
from sqlalchemy.exc import IntegrityError
urllib3.disable_warnings()

#disable warnings in case somebody (like me) is running 
#a Python version < 2.7.9


# inheriting from object is a kludge for 2.x, no longer needed in 3 if we
# migrate to that.
class TweetScraper(object):
    
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)
    
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
    
    def extract_tweet(self, tweet):
        ''' pass this either a Tweepy SearchObject or a twitter id_str: it then
        either parses the SearchObject or fetches the associated id_str tweet'''
        if isinstance(tweet, basestring):
            # if tweet is a string, that means we need to fetch the tweet
            result = self.api.get_status(tweet)
        else:
            result = tweet
        tweet_author = db.session.query(models.TwitterUser).get(
            result.user.id_str)
        if not tweet_author:
            # new user previously unseen, add to db
            tweet_author = models.TwitterUser(id_str=result.user.id_str, 
                name=result.user.screen_name)
        db.session.add(tweet_author)
        tweet_result = db.get_or_create(db.session, models.Tweet, 
            id_str=result.id_str)
        if result.in_reply_to_status_id_str:
            # if it's a reply, we want to know what tweet it's replying 
            # to
            tweet_result.reply_to_tweet_id_str = \
                result.in_reply_to_status_id_str
        if result.in_reply_to_user_id_str:
            tweet_result.reply_to_user_id_str = \
                result.in_reply_to_user_id_str
        # if any users are mentioned, probably interesting- let's get 'em
        for mentioned_user in result.entities["user_mentions"]:
            mentioned_author = db.session.query(
                models.TwitterUser).get(
                    mentioned_user["id"])
            if not mentioned_author:
                mentioned_author = models.TwitterUser(
                    id_str=mentioned_user["id_str"],
                    name=mentioned_user["screen_name"])
            db.session.add(mentioned_author)
            new_mention = models.Mention(tweet_id=result.id_str, 
                mentioned_user_id=mentioned_user["id"])
            db.session.add(new_mention)
                
                # get those hashtags in. dedupe them in case people are dumb
                # and use the same hashtag over again
        list_of_hashtags = []
        for t in result.entities["hashtags"]: list_of_hashtags.append(t["text"])
        set_of_hashtags = set(list_of_hashtags)
        for tag in set_of_hashtags:
            new_hashtag = db.session.query(models.Hashtag).get(tag.lower())
            if not new_hashtag:
                new_hashtag = models.Hashtag(text=tag.lower())
                db.session.add(new_hashtag)
            tweet_result.hashtags.append(new_hashtag)
        db.session.add(tweet_result)
        # commit it all to the db
        db.session.commit()

    
    def search_tweets(self, query):
        """ Will suck down and store results of a search in the db """
        results = self.api.search(q=query, lang="en", rpp=100)
        for result in results:
            # now let's break out the bits we're interested in
            # check if the tweet exists
            tweet_result = db.session.query(models.Tweet).get(result.id_str)
            if tweet_result:
                # entry already exists, skip it
                continue
            else:
                self.extract_tweet(result)
            
t_scraper = TweetScraper()
#t_scraper.search_tweets("Jade Helm 15")
print db.session.query(models.Tweet).first().id_str
t_scraper.extract_tweet("623020569349349376")