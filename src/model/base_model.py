from peewee import *
db = MySQLDatabase('examreg', user="root", password='', charset='utf8mb4', host='127.0.0.1', port=3306)


class BaseModel(Model):
    class Meta:
        database = db
