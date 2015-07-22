from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os.path
import models
from settings import *

engine = create_engine('sqlite:///{}'.format(
    DATABASE_NAME), convert_unicode=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance

def init_db():
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to import them first before calling init_db()
    models.Base.metadata.create_all(bind=engine)
    session.commit()
    
if __name__ == "__main__":
    init_db()

