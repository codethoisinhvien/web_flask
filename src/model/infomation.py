from peewee import *

from .base_model import BaseModel,db
from .room_seat import RoomSeat
from .schedule import Schedule
from .user import User

class Information(BaseModel):
    user_id = ForeignKeyField(User)
    schedule_id = ForeignKeyField(Schedule)
    seat_room_id = ForeignKeyField(RoomSeat)

    class Meta:
        primary_key = CompositeKey("user_id", "schedule_id", 'seat_room_id')

    def create(self,user_id,schedule_id):
        with db.cursor() as cursor:
            cursor.execute("select exam_id,subject_id,room_id from schedule INNER JOIN exam ON schedule.exam_id=exam.id where schedule.id =%s and exam.status = %s",

                        [schedule_id, 1])
            row = cursor.fetchone()
            print(row)
            cursor.execute(
                "SELECT * FROM `userexamsubject` WHERE exam_id=%s and subject_id=%s and user_id=%s and status=1",
                [row[0], row[1], user_id])

            if (cursor.fetchone() is None):
                raise Exception("Truy cập trái phép")
            cursor.execute(

                "UPDATE serexamsubjec SET status = 0 WHERE user_id = %s and exam_id = %s and subject_id =%s",
                [user_id, row[0], row[1]])

            cursor.execute(
                "UPDATE schedule SET no_of_student = no_of_student+1 WHERE id = %s",
                [self.schedule_id])

            cursor.execute(
                "Select id from roomseat  where id not in ( select seat_room_id from information where schedule_id = %s )  and room_id = %s limit 1",
                [schedule_id, row[2]])
            seat_room_id = cursor.fetchone()

            cursor.execute(
                "INSERT  into information (schedule_id,user_id,seat_room_id) VALUES( %s , %s,%s )",
                [schedule_id, user_id, seat_room_id])

