from peewee import *


from  src.model import User
from  src.model import Subject
from  src.model import Exam
db = MySQLDatabase('examreg', user="root", password='', charset='utf8mb4', host='127.0.0.1', port=3306)


def create_table():
    models= [User,Subject,Exam]
    db.drop_tables(models)
    db.create_tables(models, safe=True)
def fake_user():
    data =[
        {
            "username": 17020001,
            "password": 17020001,
            "code": 17020706,
            "full_name": "Rudolph Clynmans",
            "role": 1
        },
        {
            "username": 17020002,
            "password": 17020002,
            "code": 17020707,
            "full_name": "Nelson Guidini",
            "role": 1
        },
        {
            "username": 17020003,
            "password": 17020003,
            "code": 17020708,
            "full_name": "Ira Shay",
            "role": 1
        },
        {
            "username": 17020004,
            "password": 17020004,
            "code": 17020709,
            "full_name": "Rodina Padwick",
            "role": 1
        },
        {
            "username": 17020005,
            "password": 17020005,
            "code": 17020710,
            "full_name": "Tait Gofforth",
            "role": 1
        },
        {
            "username": 17020006,
            "password": 17020006,
            "code": 17020711,
            "full_name": "Aubert Sibbet",
            "role": 1
        },
        {
            "username": 17020007,
            "password": 17020007,
            "code": 17020712,
            "full_name": "Amabel Tapin",
            "role": 1
        },
        {
            "username": 17020008,
            "password": 17020008,
            "code": 17020713,
            "full_name": "Morgun Donnellan",
            "role": 1
        },
        {
            "username": "admin",
            "password": "admin",
            "code": 1,
            "full_name": "Le dinh thanh",
            "role": 2
        }
    ]
    with db.atomic():
        for data_dict in data:
            User.create(**data_dict)


create_table()
fake_user()
