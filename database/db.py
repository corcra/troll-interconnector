from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import models

engine = create_engine('sqlite:////home/ubuntu/workspace/troll_interconnector/test.db', convert_unicode=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
#models.Base.metadata.create_all(bind=engine)

# def init_db():
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to import them first before calling init_db()
