from flask import request,Blueprint
from src.controller.user_schedule import UserScheduleController
user_schedule= Blueprint(__name__,__name__)
url='/student/schedules'
@user_schedule.route(url,methods=['GET'])
def get_list_can_schedule():
    user= UserScheduleController()
    return user.get_list_can_schedule(11)
@user_schedule.route(url,methods=['POST'])
def resgister():
    data=request.json
    user= UserScheduleController()
    user_id=11
    return user.register(user_id,data['schedule_id'])
#codethoisinhvien
#nguyentruonggiang08
