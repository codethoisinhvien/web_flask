import datetime

from peewee import *

from .base_model import BaseModel
from .exam import Exam
from .room import Room
from .subject import Subject


class Schedule(BaseModel):
    subject_id = ForeignKeyField(Subject)
    room_id = ForeignKeyField(Room, )
    exam_id = ForeignKeyField(Exam)
    day = DateField(default=datetime.date.today)
    time_start = TimeField()
    time_end = TimeField()
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
