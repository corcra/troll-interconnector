import unittest, sys, os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from database.models import *

# tests for the scraper

class ScraperTests(unittest.TestCase):
    # set up the test database
    @classmethod
    def SetUpClass(cls):
        engine = create_engine('sqlite:///:memory:', echo=True)
        db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
        Base = declarative_base()
        Base.query = db_session.query_property()
        Base.metadata.create_all(bind=engine)
        
    def test_db_connection(self):
        # make sure db works
        test_tweet = TwitterUser(id="12345", name="test user")
        db_session.add(test_tweet)
        db_session.commit()