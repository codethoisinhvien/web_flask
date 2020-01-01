from peewee import *

from .base_model import BaseModel


class Room(BaseModel):
    name = CharField(max_length=255)
    location = TextField()
    max_student = IntegerField()
