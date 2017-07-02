from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mashup import findARestaurant
import json

from models import Restaurant, Base

engine = create_engine('sqlite:///restaurants.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/restaurants', methods=['GET', 'POST'])
def all_restaurants_handler():
    if request.method == 'GET':
        restaurants = session.query(Restaurant).all()
        restaurants = [i.serialize for i in restaurants]
        print("GET all_restaurants_handler()")
        return jsonify(restaurants)
    elif request.method == 'POST':
        location = request.args.get('location', '')
        mealType = request.args.get('mealType', '')
        restaurantInfo = findARestaurant(location=location, mealType=mealType)
        if restaurantInfo != "No Restaurants Found":
            restaurantItem = json.loads(restaurantInfo)
            restaurant_name = restaurantItem['name']
            restaurant_address = restaurantItem['address']
            restaurant_images = restaurantItem['image']
            restaurant = Restaurant(restaurant_name=str(restaurant_name, 'utf-8'),
                                    restaurant_address=str(restaurant_address, 'utf-8'),
                                    restaurant_images=str(restaurant_images, 'utf-8'))
            session.add(restaurant)
            session.commit()
            print("POST all_restaurants_handler()")
            return jsonify(restaurant.serialize)


@app.route('/restaurants/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_handler(id):
    if request.method == 'PUT':
        return "PUT restaurant_handler(%s)" % id
    if request.method == 'DELETE':
        return "DELETE restaurant_handler(%s)" % id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
