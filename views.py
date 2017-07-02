from flask import Flask, request

app = Flask(__name__)

@app.route('/restaurants', methods=['GET', 'POST'])
def all_restaurants_handler():
    if request.method == 'GET':
        return "GET all_restaurants_handler()"
    elif request.method == 'POST':
        return "POST all_restaurants_handler()"

@app.route('/restaurants/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_handler(id):
    if request.method == 'PUT':
        return "PUT restaurant_handler(%s)" % id
    if request.method == 'DELETE':
        return "DELETE restaurant_handler(%s)" % id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)