from flask import request, Blueprint

from src.controller.user_schedule import UserScheduleController
from src.common.authentication import token_required,is_admin
user_schedule = Blueprint(__name__, __name__)
url = '/student/schedules'


@user_schedule.route(url, methods=['GET'])

@token_required

def get_list_can_schedule():
    user = UserScheduleController()
    user_id=request.user['id']
    return user.get_list_can_schedule(user_id)


@user_schedule.route(url, methods=['POST'])
@token_required
def resgister():
    data = request.json
    user = UserScheduleController()
    user_id = request.user['id']
    return user.register(user_id, data['schedule_id'])


@user_schedule.route(url + '/<int:id>', methods=['DELETE'])
@token_required

def delete(id):
    user = UserScheduleController()
    user_id = request.user['id']
    print(id)
    return   user.delete(user_id,id)
@user_schedule.route('/student/myschedules', methods=['GET'])
@token_required

def get_my_schedule():
    user = UserScheduleController()
    user_id = request.user['id']
    print(id)
    return   user.get_my_list_schedule(user_id)

# codethoisinhvien
# nguyentruonggiang08
