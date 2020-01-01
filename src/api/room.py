from flask import Blueprint

from src.controller.room_controller import RoomController
room = Blueprint(__name__, __name__)


@room.route('/rooms', methods=['GET'])
def get_list():
    room = RoomController()
    return room.get_list()
