from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_0]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class Student:
    db = "dojo_fruit_store"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_student(cls, data):
        query = """
        INSERT INTO students (name) VALUES (%(name)s)
        ;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        return results