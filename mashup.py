from geocode import getGeocodeLocation 
import httplib2
import json

import sys
import codecs

def findARestaurant(mealType, location):
	 Foursquare_CLIENT_ID = "APRMJQQN4K2CYIAQSMPQBWRTHFTWYGHBCSGMZRQOMHNFPPJR"
	 Foursquare_CLIENT_SECRET = "HBEQC1TILOBCAHSBEC020AQPP2VRCZVWFXAPB1L1LS4O2VJW"
     latitude, longitude = getGeocodeLocation(location)
	 url = ('https://api.foursquare.com/v2/venues/search?ll=%s,%s&client_id=%s&client_secret=%s' % (latitude, longitude, Foursquare_CLIENT_ID, Foursquare_CLIENT_SECRET))
	 h =httplib2.Http()
	 response, content = h.request(url,"GET")
	 response_json =json.load(response)
	 print response_json


     

if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")