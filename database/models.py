from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, Float, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

tweets_hashtags_table = Table('association', Base.metadata,
                              Column('tweets_id', Integer, ForeignKey('tweets.id')),
                              Column('hashtags_id', Integer, ForeignKey('hashtags.id'))
                              )

class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(BigInteger, primary_key=True)
    content = Column(Text)
    author = Column(BigInteger, ForeignKey('twitteruser.id'))
    hashtags = relationship("Hashtag", secondary=tweets_hashtags_table, backref="tweets")
    reply_to_id = Column(BigInteger)
    reply_to_user_id = Column(BigInteger)

class TwitterUser(Base):
    __tablename__ = 'twitter_users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tweets_id = Column(BigInteger, ForeignKey('tweets.id'))
    tweets = relationship("Tweet", backref="twitter_user")
    troll_score = Column(Float, default=0)

class Hashtag(Base):
    __tablename__ = 'hashtags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class Mention(Base):
    __tablename__ = 'mentions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tweet = Column(Integer, ForeignKey('tweet.id'))
    mentioned_user = Column(Integer, ForeignKey('twitteruser.id'))