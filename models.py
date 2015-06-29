from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from troll_interconnector import Base

tweets_hashtags_table = Table('association', Base.metadata,
                              Column('tweets_id', Integer, ForeignKey('tweets.id')),
                              Column('hashtags_id', Integer, ForeignKey('hashtags.id'))
                              )

class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text)
    author = Column(Integer, ForeignKey('twitteruser.id'))
    hashtags = relationship("Hashtag", secondary=tweets_hashtags_table, backref="tweets")

class TwitterUser(Base):
    __tablename__ = 'twitter_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    tweets = relationship("Tweet", backref="twitter_user")
    troll_score = Column(Float)

class Hashtag(Base):
    __tablename__ = 'hashtags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class Mention(Base):
    __tablename__ = 'mentions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tweet = Column(Integer, ForeignKey('tweet.id'))
    mentioned_user = Column(Integer, ForeignKey('twitteruser.id'))