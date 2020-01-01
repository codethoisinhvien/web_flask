from peewee import *

from .base_model import BaseModel


class Seat(BaseModel):
    name = CharField(max_length=255)
