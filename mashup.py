from geocode import getGeocodeLocation
import httplib2
import json

import sys
import codecs

Foursquare_CLIENT_ID = "APRMJQQN4K2CYIAQSMPQBWRTHFTWYGHBCSGMZRQOMHNFPPJR"
Foursquare_CLIENT_SECRET = "HBEQC1TILOBCAHSBEC020AQPP2VRCZVWFXAPB1L1LS4O2VJW"


def findARestaurant(mealType, location):
    latitude, longitude = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&ll=%s,%s&query=%s&v=20160601' % (Foursquare_CLIENT_ID, Foursquare_CLIENT_SECRET, latitude, longitude, mealType))
    h = httplib2.Http()
    response, content = h.request(url)
    response_json = json.loads(content)
    if response_json['response']['venues']:
        restaurant = response_json['response']['venues'][0]
        restaurant_name = restaurant['name']
        venue_id = restaurant['id']
        restaurant_address = restaurant['location']
        address = ""
        for i in restaurant_address:
            address += i + " "
        restaurant_address = address
        restaurant_imageURL = getRestaurantImageURL(venue_id)
        restaurantInfo = {'name': restaurant_name,
                          'address': restaurant_address,
						  'image': restaurant_imageURL}
        print "Restaurant Name: %s" % restaurantInfo['name']
        print "Restaurant Address: %s" % restaurantInfo['address']
        print "Image: %s \n" % restaurantInfo['image']
        return restaurantInfo
    else:
        print "No Restaurants Found for %s" % location
        return "No Restaurants Found"
    


def getRestaurantImageURL(venue_id):
    h = httplib2.Http()
    url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=20150603' % (venue_id, Foursquare_CLIENT_ID, Foursquare_CLIENT_SECRET))
    response, content = h.request(url, "GET")
    imgInfo_json = json.loads(content)
    if imgInfo_json['response']['photos']['items']:
        firstpic = imgInfo_json['response']['photos']['items'][0]
        prefix = firstpic['prefix']
        suffix = firstpic['suffix']
        imageURL = prefix + '300x300' + suffix
    else:
        imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"
    return imageURL

if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    # findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney Australia")
