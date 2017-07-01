import httplib2
import json

def getGeocodeLocation(inputString):
    google_api_key = 'AIzaSyDcf-b4XtBdoBzpX8bJHflIhEqt6_KGE1M'
    locationString = inputString.replace(' ', '+')
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (locationString, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    #print response
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)