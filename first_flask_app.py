#from flask import Flask
import flask
from flask import Flask

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
    pass

#GET /store/<string:name>
@app.route('/store/<string:name>') #<string:name> este name debe ser igual al parametro get_store(name):
def get_store(name): #http://127.0.0.1:5000/name --> este es el 'name'
    pass

#GET /store
@app.route('/store')
def get_stores():
    pass

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST']) #<string:name> este name debe ser igual al parametro get_store(name):
def create_item_in_store(name): #http://127.0.0.1:5000/name --> este es el 'name'
    pass

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item') #<string:name> este name debe ser igual al parametro get_store(name):
def get_item_in_store(name): #http://127.0.0.1:5000/name --> este es el 'name'
    pass

#app.run(port=5000)