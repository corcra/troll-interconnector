#!/bin/python
# Class for tweeps
# 
# HOW TO OOP ?


import numpy as np
import database.db as db
import database.models as models
class tweep(object):
    """
    oh god
    """
    def __init__(self, tweep_author):
        """
        wat
        """
        # need interaction with the database here
        # for now just grabs tweets from db- tomorrow will make sure it fetches
        # any tweets that don't exist in db
        tweets = db.session.query(models.Tweets).filter(author=tweep_author)
        # not saving followers in the db, will add that tomorrow as well
        followers = ['placeholder', 'placeholder']
        self.tweets = tweets
        self.followers = followers
        # and so on and so forth
    def calculate_troll_score(self):
        """
        define a 'troll probability' (in [0, 1])
        Some ideas for features:
            - % of tweets that are insulting
            - % of tweets that are @-replies
            - ???
        """
        # magic machine learning goes here
        # so spooky and magical
        score = np.random.random()
        self.score = score
        return True
    def calculate_ideology(self):
        """
        for now I'm assuming ideology is a vector
        NOTE: we may not want to go down this route
        ... depends on if we have any good idea of how to obtain these vectors
        """
        # even more magical machine learning
        ideology_dimension = 5
        ideology = np.random.normal(ideology_dimension)
        self.ideology = ideology
        return True
