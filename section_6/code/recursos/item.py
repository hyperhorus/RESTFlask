import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from modelos.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank!")


    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message':'Item not found'}, 404


    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f"an item with name {name} already exists"}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            ItemModel.save_to_db(item)
        except:
            return {"message": f"{item}An error ocurred inserting the item."}, 500 #internal server error

        return item.json(), 201   #indica que el item fue creado


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": f"{name} deleted"}


    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item == None:
            item = ItemModel(name, data['price'])
        else:
            updated_item.update()
        item.save_to_db()

        return item.json()

class ItemList(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        items = []

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        for row in result:
            items.append({'name': row[0], 'price':row[1]})
        connection.close()
        return {'items': items}

        #return {'items': 'No items found'}
