import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    email = Column(String(80), nullable = False)
    picture = Column(String(80))

    @property
    def serialize(self):
        return {
            'name' : self.name,
            'id' : self.id,
            'email' : self.email,
            'picture' : self.picture,
        }

class Category(Base):
    __tablename__ = 'category'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name' : self.name,
            'id' : self.id,
            'user_id' : self.user_id,
        }

class Item(Base):
    __tablename__ = 'item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name' : self.name,
            'id' : self.id,
            'description' : self.description,
            'user_id' : self.user_id,
        }

engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.create_all(engine)
