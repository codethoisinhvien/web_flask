from peewee import *

from .base_model import BaseModel, db
from .room_seat import RoomSeat
from .schedule import Schedule
from .user import User
from .room import Room
from .seat import Seat
from .exam import Exam

from .subject import Subject
class Information(BaseModel):
    user_id = ForeignKeyField(User)
    schedule_id = ForeignKeyField(Schedule)
    seat_room_id = ForeignKeyField(RoomSeat)

    class Meta:
        primary_key = CompositeKey("user_id", "schedule_id", 'seat_room_id')

    def create(self, user_id, schedule_id):
        with db.atomic() as transaction:
            try:
                with db.cursor() as cursor:
                    cursor.execute(
                        "select exam_id,subject_id,room_id from schedule INNER JOIN exam ON schedule.exam_id=exam.id where schedule.id =%s and exam.status = %s",

                        [schedule_id, 1])
                    row = cursor.fetchone()
                    print(row)
                    cursor.execute(
                        "SELECT * FROM `userexamsubject` WHERE exam_id=%s and subject_id=%s and user_id=%s and status=1",
                        [row[0], row[1], user_id])

                    if (cursor.fetchone() is None):
                        raise Exception("Truy cập trái phép")
                    cursor.execute(

                        "UPDATE userexamsubject SET status = 0 WHERE user_id = %s and exam_id = %s and subject_id =%s",
                        [user_id, row[0], row[1]])

                    cursor.execute(
                        "UPDATE schedule SET no_of_student = no_of_student+1 WHERE id = %s",
                        [schedule_id])

                    cursor.execute(
                        "Select id from roomseat  where id not in ( select seat_room_id from information where schedule_id = %s )  and room_id = %s limit 1",
                        [schedule_id, row[2]])
                    seat_room_id = cursor.fetchone()

                    cursor.execute(
                        "INSERT  into information (schedule_id,user_id,seat_room_id) VALUES( %s , %s,%s )",
                        [schedule_id, user_id, seat_room_id])
            except:
                transaction.rollback()
                raise "Có lỗi xảy ra"

    def delete_register(self, user_id, schedule_id):
        print(user_id, schedule_id)

        with db.atomic() as transaction:
            try:
                with db.cursor() as cursor:
                    cursor.execute("select user_id  from  information where schedule_id=%s and  user_id =%s",
                                   [schedule_id, user_id])

                    if cursor.fetchone() is None:
                        raise Exception("Dữ liệu không tồn tại")
                    # xóa bản ghi (shedule_id,user_id)
                    cursor.execute("delete  from  information where schedule_id=%s and  user_id =%s",
                                   [schedule_id, user_id])
                    # thay đổi số học viên(schedule_id)
                    cursor.execute("SELECT exam_id,subject_id FROM schedule WHERE id =%s",
                                   [schedule_id])
                    row = cursor.fetchone()
                    cursor.execute(
                        "UPDATE schedule SET no_of_student = no_of_student-1 WHERE id = %s",
                        [schedule_id])
                    # Thay đổi trang thái(user_id,subject_id,exam_id)
                    cursor.execute(
                        "UPDATE userexamsubject SET status = 1 WHERE user_id=%s and subject_id =%s and exam_id = %s",
                        [user_id, row[1], row[0]])
            except:
                transaction.rollback()
                raise "Có lỗi xảy ra"
    def get_schedule_in_student(self,user_id):
            query = Information.select().where(Information.user_id==user_id).join(RoomSeat).join(Room).switch(Information)\
                .join(Schedule).\
                switch(RoomSeat).join(Seat)\
                .switch(Schedule).join(Subject) \
                .switch(Schedule).join(Exam)\
                .select(
                Room.name.alias("room"),
                Schedule.id.alias("schedule_id"),
                Seat.name.alias("seat"),
                Subject.name.alias("subject"),
                Exam.name.alias("exam"),
                Schedule.day,
                Schedule.time_start,
                Schedule.time_end

            ).dicts()
            return query

    def get_student_in_schedule(self, schedule_id):

        query = Information.select().where(Information.schedule_id == schedule_id).join(RoomSeat).join(Room).switch(
            Information) \
            .join(Schedule) \
            .switch(RoomSeat).join(Seat) \
            .switch(Schedule).join(Subject) \
            .switch(Schedule).join(Exam) \
            .switch(Information).join(User) \
            .select(
            Room.name.alias("room"),
            Schedule.id.alias("schedule_id"),
            Seat.name.alias("seat"),
            Subject.name.alias("subject"),
            Exam.name.alias("exam"),
            Schedule.day,
            Schedule.time_start,
            Schedule.time_end,
            User.code,
            User.full_name,

        ).dicts()
        return query
