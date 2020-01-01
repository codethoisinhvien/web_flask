from flask import Blueprint

from src.controller.room_controller import RoomController
room = Blueprint(__name__, __name__)
from src.common.authentication import token_required,is_admin

@room.route('/rooms', methods=['GET'])
@token_required
@is_admin
def get_list():
    room = RoomController()
    return room.get_list()
