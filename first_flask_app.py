#from flask import Flask
import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name':'My wonderful store',
        'items': [
            {
                'name':'my item',
                'prices': 15.99
            }
        ]
    }
]

#POST /store data: {name:}
#Esto crea un endpoint...si un endpoin pero debe ser post, porque debemos crear la store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>') #<string:name> este name debe ser igual al parametro get_store(name):
def get_store(name): #http://127.0.0.1:5000/name --> este es el 'name'
    # iterate over stores
    for store in stores:
        # if the store name matches, return it
        if store['name'] == name:
            return jsonify(store)
    # if none match, return an error
    return jsonify({'message': 'Store not found'})

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST']) #<string:name> este name debe ser igual al parametro get_store(name):
def create_item_in_store(name): #http://127.0.0.1:5000/name --> este es el 'name'
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found'})

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item') #<string:name> este name debe ser igual al parametro get_store(name):
def get_item_in_store(name): #http://127.0.0.1:5000/name --> este es el 'name'
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'Store not found'})

#app.run(port=5000)