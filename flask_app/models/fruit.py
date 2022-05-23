from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session

class Fruit:
    db = "dojo_fruit_store"
    def __init__(self, data):
        self.id = data['id']
        self.strawberry = data['strawberry']
        self.raspberry = data['raspberry']
        self.apple = data['apple']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
