import unittest
import sqlalchemy
from .. import models

# tests for the tweet scraper

class ScraperTests(unittest.TestCase):
    # set up the test database
    @classmethod
    def SetUpClass(cls):
        engine = create_engine('sqlite:///:memory:', echo=True)
        # set up database stuff here
        
    def test_search_endpoint(self):
        # make the search call, should return with a message OK and valid JSON
        pass