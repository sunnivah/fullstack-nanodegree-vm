import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

######## class and table definition ########

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    title = Column(String(20), nullable = False)

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key = True)
    title = Column(String(20), nullable = False)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey(Category.id))
    category_relationship = relationship(Category)

    #Serialize function to send Item JSON objects serialized
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'description' : self.description
       }

class User(Base):
    __tablename__ = 'user'

    username = Column(Integer, primary_key = True)
    password = Column(String(20), nullable = False)

engine = create_engine('sqlite:///itemCatalog.db')
Base.metadata.create_all(engine)