from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) #facilita la creación de resoruces

items = []



class Item(Resource):
    def get(self, name):
        for it in items:
            if it['name'] == name:
                return it
        return {'item': None}, 404  #este numero hace que el codigo de error sea el 404, de Not Found


    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201   #indica que el item fue creado

api.add_resource(Item, '/item/<string:name>')