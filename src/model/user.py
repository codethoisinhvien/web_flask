from peewee import *

from .base_model import BaseModel


class User(BaseModel):
    username = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)
    code = CharField(max_length=255)
    full_name = CharField(max_length=255)
    role = IntegerField(default=1)

    def get_user_by_username(self, username):
        query = self.select().where(username=username).limit(1)
        print(query)
        return query.execute();
