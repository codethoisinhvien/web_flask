from trace import Trace

from peewee import *


from .base_model import BaseModel
from .exam import Exam
from .subject import Subject
from .user import User
from .schedule import Schedule
from .room import Room

class UserExamSubject(BaseModel):
    id = UUIDField(unique=True)
    subject_id = ForeignKeyField(Subject,backref='subjects',related_name='dogs')
    user_id = ForeignKeyField(User)
    exam_id = ForeignKeyField(Exam)
    status = BooleanField(default=True)
    be_register = BooleanField(default=True)

    class Meta:
        primary_key = CompositeKey("subject_id", "user_id","exam_id")
    def get_list(self):
        query=UserExamSubject.select().join(User).switch(UserExamSubject).join(Exam).switch(UserExamSubject).select(Exam.name.alias('exam'),Subject.name.alias('subject'),User.full_name,User.code,UserExamSubject.id,UserExamSubject.be_register).join(Subject).dicts()
        return query

    def get_list_can_schedule(self,user_id):
        query =Schedule.select().join(Room).switch(Schedule).join(Subject).join(UserExamSubject).where(UserExamSubject.user_id==user_id).join(Exam).where(Exam.status==True).select(
            Exam.name.alias('exam'),
            UserExamSubject.status,
            UserExamSubject.be_register,
            Schedule.id.alias("schedule_id"),
            Schedule.day,
            Schedule.time_end,
            Schedule.time_start,
            Schedule.no_of_student,
            Room.max_student,
            Room.name.alias("room"),
           Subject.name.alias("subject")).dicts()
        return query
