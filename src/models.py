import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(Integer, nullable=False)
    address = Column(String(250), nullable=False)
    created = Column(DateTime, nullable=False )
    privacity = Column(String, nullable=False)
    posts = relationship('Post',backref='user',lazy=True)
    sources = relationship('Source',backref='user',lazy=True)
    tags = relationship('Tag',backref='user',lazy=True)
    changeusernames = relationship('Changeusername',backref='user',lazy=True)
    followers = relationship('Follow',backref='user',lazy=True)
    comments = relationship('Comment',backref='user',lazy=True)
    likes = relationship('Like',backref='user',lazy=True)

class Post(Base):
    __tablename__ = 'post'        
    id = Column(Integer, primary_key=True)
    is_reel = Column(Boolean,  nullable=False)
    is_sensitivecontent = Column(Boolean,  nullable=False)
    is_highlighted = Column(Boolean,  nullable=False)
    source_id = Column(Integer,ForeignKey('source.id'))
    backgroundsong_id = Column(Integer,ForeignKey('backgroundsong.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    tags = relationship('Tag',backref='post',lazy=True)
    comments = relationship('Comment',backref='post',lazy=True)
    likes = relationship('Like',backref='post',lazy=True)

class Source(Base):
    __tablename__ = 'source'        
    id = Column(Integer, primary_key=True)    
    user_id = Column(Integer, ForeignKey('user.id'))
    url = Column(String(250),nullable=False)
    size = Column(String(250),nullable=False)
    duration = Column(Integer,nullable=False)
    posts = relationship('Post',backref='source',lazy=True)
    stories = relationship('Story',backref='source',lazy=True)

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    location = Column(String(250), nullable=False)
    description = Column(String(250),nullable=False)
    tag_id = Column(Integer,ForeignKey('tag.id'))
    source_id = Column(Integer,ForeignKey('source.id'))
    
class Backgroundsong(Base):
    __tablename__ = 'backgroundsong'        
    id = Column(Integer, primary_key=True)    
    name = Column(String(80),nullable=False)
    duration = Column(Integer,nullable=False)
    author = Column(String(80),nullable=False)
    band = Column(String(80),nullable=False)
    posts = relationship('Post',backref='backgroundsong',lazy=True)
    
class Tag(Base):
    __tablename__ = 'tag'        
    id = Column(Integer, primary_key=True)    
    user_id = Column(Integer,ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    stories = relationship('Story',backref='tag',lazy=True)

class ChangeUsername(Base):
    __tablename__ = 'changeusername'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    oldname = Column(Integer,nullable=False)
    newname = Column(Integer,nullable=False)

class Follow(Base):
    __tablename__ = 'follower'
    id = Column(Integer,primary_key=True)
    fromuser_id = Column(Integer,ForeignKey('user.id'))
    touser_id = Column(Integer,ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer,primary_key=True)
    commentary = Column(String(250),primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))
    post_id = Column(Integer,ForeignKey('post.id'))
    likes = relationship('Like',backref='comment',lazy=True)

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    post_id = Column(Integer,ForeignKey('post.id'))
    comment_id = Column(Integer,ForeignKey('comment.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
