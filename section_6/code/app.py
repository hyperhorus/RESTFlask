from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from modelos.user import UserModel
from recursos.item import Item, ItemList
from recursos.users import UserRegister
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app) #facilita la creación de resoruces
db.init_app(app)
jwt = JWT(app, authenticate, identity) #Esto crea un endpoint nuevo, /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

#if __name__ == '__main__':
