from peewee import *

from .base_model import BaseModel


class Subject(BaseModel):
    name = CharField(max_length=255, unique=True)
    code = CharField(max_length=255, unique=True, )
