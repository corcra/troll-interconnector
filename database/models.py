from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, Float, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

tweets_hashtags_table = Table('association', Base.metadata,
                              Column('tweets_id', BigInteger, ForeignKey('tweets.id')),
                              Column('hashtags_id', BigInteger, ForeignKey('hashtags.id'))
                              )

class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    id_str = Column(String, unique=True)
    content = Column(Text)
    author_id = Column(BigInteger, ForeignKey('twitter_users.id'))
    author = relationship("TwitterUser", backref="tweets")
    # hashtags = relationship("Hashtag", secondary=tweets_hashtags_table, 
    #     backref="tweets")
    reply_to_tweet_id_str = Column(String, nullable=True)
    reply_to_user_id_str = Column(String, nullable=True)

class TwitterUser(Base):
    __tablename__ = 'twitter_users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    troll_score = Column(Float, default=0)

class Hashtag(Base):
    __tablename__ = 'hashtags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class Mention(Base):
    __tablename__ = 'mentions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tweet = Column(BigInteger, ForeignKey('tweets.id'))
    mentioned_user = Column(Integer, ForeignKey('twitter_users.id'))