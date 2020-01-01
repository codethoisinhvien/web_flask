from peewee import *

from src.model import Exam
from src.model import Room
from src.model import Subject
from src.model import User
from src.model import UserExamSubject, Schedule, RoomSeat, Seat, Information

db = MySQLDatabase('examreg', user="root", password='', charset='utf8mb4', host='127.0.0.1', port=3306)


def create_table():
    models = [User, Subject, Exam, Room, UserExamSubject, Schedule, RoomSeat, Seat, Information]
    db.drop_tables(models)
    db.create_tables(models, safe=True)


def fake_user():
    data = [
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


def fake_room():
    data = [{"name": "1", "location": "5861 Cody Trail", "max_student": 100},
            {"name": "2", "location": "0 Sherman Center", "max_student": 2},
            {"name": "3", "location": "98527 Thierer Crossing", "max_student": 100},
            {"name": "4", "location": "46586 Forest Dale Hill", "max_student": 100},
            {"name": "5", "location": "38 Butternut Alley", "max_student": 100},
            {"name": "Phòng đặc biệt", "location": "5129 Talmadge Parkway", "max_student": 100}]
    with db.atomic():
        for data_dict in data:
            Room.create(**data_dict)


def fake_subject():
    data = [{"name": "Phát triển ứng dụng web", "code": "INT 3306"},
            {"name": "Trí tuệ nhân tạo ", "code": "INT 3305"}

            ]
    with db.atomic():
        for data_dict in data:
            Subject.create(**data_dict)


def fake_exam():
    data = [{"name": "Kì thi Học kì 1", "status": True},

            ]
    with db.atomic():
        for data_dict in data:
            Exam.create(**data_dict)


def fake_seat():
    data= [{"name": str(i),}for i in range(100)]


    with db.atomic():
        for data_dict in data:
            Seat.create(**data_dict)
def fake_room_seat():


    with db.atomic():
        for i in range(100):
            for j in range(7):
                if j>0 and i>0:
                     RoomSeat.create(room_id=j,seat_id=i)

create_table()
fake_user()
fake_room()
fake_subject()
fake_exam()
fake_seat()
fake_room_seat()
