#!/bin/python
# madbot functions, in pseudo pseudocode form (for now)

import numpy as np

def is_insulting(tweet):
    """
    Outputs probability that a given tweet is insulting.
    Using amueller's model.
    Test:
    >>> is_insulting('fuck you')
    1
    >>> is_insulting('hello')
    0
    """
    cv = np.load('./ML/insult_cv.npy').item()
    svm = np.load('./ML/insult_svm.npy').item()
    tweet_transformed = cv.transform([tweet])
    score = svm.predict(tweet_transformed)[0]
    return score

def get_argument_score(user1, user2):
    """
    Considers two twitter users and calculates some proxy of 
        'probability of argument' between them.
    Score is either in [0, 1] or {0, 1} (undecided)
    """
    # this is likely going to be a binary classifier 
    # or logistic regression model
    #
    # required:
    #   features (notably, numerical representation of such)
    #   pretrained model
    #
    # pretrained model requires:
    #   features
    #   training data!
    score = 0.5
    return score

def get_target(selector):
    """
    Identify a target to neutralise.
    selector is either a hashtag, or a username.
        (or something else I haven't thought of, I guess)
    """
    # if selector is a hashtag:
    #   need to scan the database of tweets using that hashtag
    #   score participants by trollishness
    #   return biggest asshole
    #
    # if selector is a user:
    #   we are done!
    #   return user
    #
    # TODO ALL
    username = '@realDonaldTrump'        # placeholder, obviously
    return username

def get_match(target, selector):
    """
    Find a partner for 'target'.
    target is a username
    selector is a hashtag
        or something else, potentially a topic (haven't thought of this)
    """
    # if target has an 'ideology' attribute:
    #   if we have a troll database:
    #       find one with largest ideology difference
    #   if we have a tweet database:
    #       identify trolls in tweets
    #       find one with largest ideology difference
    # if target does not have an 'ideology' attribute:
    #   if we have a troll database:
    #       loop through, calculating *pairwise* argumentative score
    #   if we have a tweet database:
    #       identify trolls in tweets
    #       loop through, calculating *pairwise* argumentative score
    #
    # relevance of 'selector' is that we could use 
    # it to subset the tweet/troll database
    #
    # ... I guess?
    # TODO ALL
    match_username = '@TrumpAsAnime'
    return match_username

def form_connection(target, match, selector):
    """
    Construct the perfect tweet to spark troll romance.
    """
    # ??? ???
    tweet = 'lol ur an idiot ' + target + ', read what ' +  match
    tweet += ' said about ' + selector
    # ??? ???
    assert len(tweet)<=140
    return tweet
