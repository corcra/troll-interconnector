from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

# create our DB base
Base = declarative_base()


tweets_hashtags_table = Table('association', Base.metadata,
                              Column('tweets_id', Integer, ForeignKey('tweets.id')),
                              Column('hashtags_id', Integer, ForeignKey('hashtags.id'))
                              )

class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text)
    author = Column(Integer, ForeignKey('author.id'))
    hashtags = relationship("Hashtag", secondary=tweets_hashtags_table, backref="tweets")

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    tweets = relationship("Tweet", backref="author")
    troll_score = Column(Float)

class Hashtag(Base):
    __tablename__ = 'hashtags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

