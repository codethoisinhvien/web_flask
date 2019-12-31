from peewee import *

from .base_model import BaseModel


class Exam(BaseModel):
    name = CharField(max_length=255, unique=True)
    status = BooleanField(default=False)
