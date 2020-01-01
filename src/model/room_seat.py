from peewee import *

from .base_model import BaseModel
from .seat import Seat
from  .room import Room
class RoomSeat(BaseModel):
    room_id = ForeignKeyField(Room)
    seat_id = ForeignKeyField(Seat)
    class Meta:
       indexes = (
           (("seat_id", "room_id"), True),
       )
