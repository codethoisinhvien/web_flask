import datetime

from peewee import *

from .base_model import BaseModel, db
from .room_seat import RoomSeat

from .subject import Subject
from .room import Room
from .seat import Seat
from .exam import Exam
from .user import User



class Schedule(BaseModel):
    subject_id = ForeignKeyField(Subject)
    room_id = ForeignKeyField(Room, )
    exam_id = ForeignKeyField(Exam)
    day = DateField(default=datetime.date.today,null=False)
    time_start = TimeField(null=False)
    time_end = TimeField(null=False)
    no_of_student = IntegerField(default=0)

    def get_list(self):
        query = Exam.select().join(Schedule).join(Room).switch(Schedule).join(Subject).select(Exam.id.alias('exam_id'),
                                                                                              Exam.name.alias('exam'),
                                                                                              Room.id.alias('room_id'),
                                                                                              Room.name.alias('room'),
                                                                                              Room.max_student,
                                                                                              Subject.id.alias(
                                                                                                  'subject_id'),
                                                                                              Subject.name.alias(
                                                                                                  'subject'),
                                                                                              Schedule
                                                                                              ).dicts()
        return query




