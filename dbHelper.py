from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

from mashup import findARestaurant
from models import Restaurant, Base

engine = create_engine('sqlite:///restaurants.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def clear_data(session):
    meta = Base.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()

def populateData():
    restaurantExamples = {
        findARestaurant("Falafel", "Cairo, Egypt"),
        findARestaurant("Pizza", "Tokyo, Japan"),
        findARestaurant("Tacos", "Jakarta, Indonesia"),
        findARestaurant("Tapas", "Maputo, Mozambique"),
        findARestaurant("Spaghetti", "New Delhi, India"),
        findARestaurant("Cappuccino", "Geneva, Switzerland"),
        findARestaurant("Sushi", "Los Angeles, California"),
        findARestaurant("Steak", "La Paz, Bolivia"),
        findARestaurant("Gyros", "Sydney Australia")
    }
    return restaurantExamples


def addItems(session):
    restaurantExamples = populateData()
    for item in restaurantExamples:
        ItemInfo = json.loads(item)
        restaurant = Restaurant(restaurant_name = str(ItemInfo['name']),
                                restaurant_address = str(ItemInfo['address']),
                                restaurant_images = str(ItemInfo['image']))
        session.add(restaurant)
        session.commit()


if __name__ == '__main__':
    clear_data(session)
    addItems(session)
