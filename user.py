from flask_login import UserMixin
from db import get_db

UserCollectionName = "Users"


class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):
        db = get_db()
        if db.hasCollection(UserCollectionName):
            users = db[UserCollectionName]
        else:
            users = db.createCollection(name=UserCollectionName)
        try:
            user_doc = users[user_id]
            return User(id_=user_doc['_key'], name=user_doc['name'], email=user_doc['email'], profile_pic=user_doc['profile_pic'])
        except:
            return None


    @staticmethod
    def create(id_, name, email, profile_pic):
        db = get_db()
        if db.hasCollection(UserCollectionName):
            users = db[UserCollectionName]
        else:
            users = db.createCollection(name=UserCollectionName)
        user_doc = users.createDocument()
        user_doc['name'] = name
        user_doc['email'] = email
        user_doc['profile_pic'] = profile_pic
        user_doc._key = id_
        user_doc.save()