import unittest, sys, os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import database.models as models

# tests for the scraper


class ScraperTests(unittest.TestCase):
    # set up the test database

    def setUp(self):
        engine = create_engine('sqlite:///:memory:', echo=True)
        models.Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        self.db_session = Session()
        
    def test_db_connection(self):
        # make sure db works
        test_user = models.TwitterUser(id="12345", name="test user")
        self.db_session.add(test_user)
        self.db_session.commit()
        test_retrieve = self.db_session.query(models.TwitterUser).filter_by(
            name="test user").first()
        self.assertEqual("test user", test_retrieve.name)
        
    
        
if __name__ == '__main__':
    unittest.main()