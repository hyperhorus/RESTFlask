import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank!")


    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)

        if item:
            return item
        return {'message':'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    def post(self, name):
        if self.find_by_name(name):
            return {'message': f"an item with name {name} already exists"}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

        return item, 201   #indica que el item fue creado

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name =?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {"message": f"{name} deleted"}

    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        if item == None:
            item = {'name': name, 'price': data['price']}
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "INSERT INTO items VALUES (?, ?)"
            cursor.execute(query, (item['name'], item['price']))
            connection.commit()
            connection.close()

            #items.append(item)
        else:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query = "UPDATE items SET name =?, price=?"
            cursor.execute(query, (item['name'], item['price']))
            connection.commit()
            connection.close()

        return item

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)

        if result:
            row = result.fetchall()
            connection.close()
            return row

        return {'items': 'No items found'}

