from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, Float, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

tweets_hashtags_table = Table('association', Base.metadata,
                              Column('tweets_id', String, ForeignKey('tweets.id_str')),
                              Column('hashtags_text', String, ForeignKey('hashtags.text'))
                              )
    
followers_table = Table('followers_table', Base.metadata,
            Column('t_users_id', String, ForeignKey('twitter_users.id_str')),
            Column('f_users_id', String, ForeignKey('twitter_users.id_str'))
            )
                              

class Tweet(Base):
    __tablename__ = 'tweets'

    id_str = Column(String, primary_key=True)
    content = Column(Text)
    author_id = Column(String, ForeignKey('twitter_users.id_str'))
    author = relationship("TwitterUser", backref="tweets")
    hashtags = relationship("Hashtag", secondary=tweets_hashtags_table, 
         backref="tweets")
    reply_to_tweet_id_str = Column(String, nullable=True)
    reply_to_user_id_str = Column(String, nullable=True)

class TwitterUser(Base):
    __tablename__ = 'twitter_users'

    id_str = Column(String, primary_key=True)
    name = Column(String)
    troll_score = Column(Float, default=0)
    followers = relationship("TwitterUser",
                        secondary=followers_table,
                        primaryjoin="TwitterUser.id_str==followers_table.c.t_users_id",
                        secondaryjoin="TwitterUser.id_str==followers_table.c.f_users_id",
                        backref="parents"
                        )
class Hashtag(Base):
    __tablename__ = 'hashtags'

    text = Column(String, primary_key=True)

class Mention(Base):
    __tablename__ = 'mentions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tweet_id = Column(String, ForeignKey('tweets.id_str'))
    tweet = relationship("Tweet", backref="mentions")
    mentioned_user_id = Column(String, ForeignKey('twitter_users.id_str'))
    mentioned_user = relationship("TwitterUser", backref="user")