from sqlalchemy import Column, INTEGER, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(INTEGER, primary_key=True)
    restaurant_name = Column(String, nullable=False)
    restaurant_address = Column(String)
    restaurant_images = Column(String)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'restaurant_name': self.restaurant_name,
            'restaurant_address': self.restaurant_address,
            'restaurant_images': self.restaurant_images
        }


engine = create_engine('sqlite:///restaurats.db')
Base.metadata.create_all(engine)