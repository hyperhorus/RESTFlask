from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) #facilita la creación de resoruces

items = []



class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'], items), None)
        return {'item': None}, 200 if item else 404


    def post(self, name):
        if next(filter(lambda x: x['name'], items), None):
            return {'message': f"an item with name {name} already exists"}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201   #indica que el item fue creado

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')