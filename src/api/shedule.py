from flask import Blueprint, request

from src.controller.shedule_controller import ScheduleController
from src.common.authentication import token_required,is_admin
schedule = Blueprint(__name__, __name__)


@schedule.route('/schedules', methods=['GET'])
@token_required
@is_admin
def get_list():
    schedule = ScheduleController()
    return schedule.get_list()


@schedule.route('/schedules', methods=['POST'])
@token_required
@is_admin
def create():
    data = request.json
    schedule = ScheduleController()
    return schedule.create(data['exam_id'], data['room_id'], data['subject_id'], data['day'], data['start_time'],
                           data['end_time'])
@schedule.route('/schedules/<int:id>', methods=['PUT'])
@token_required
@is_admin
def update(id):
    data = request.json
    schedule = ScheduleController()
    return schedule.update(id,data['exam_id'], data['room_id'], data['subject_id'], data['day'], data['start_time'],
                           data['end_time'])
@schedule.route('/schedules/<int:id>', methods=['DELETE'])
@token_required
@is_admin
def delete(id):
    schedule = ScheduleController()
    return schedule.delete(id)
@schedule.route('/schedules/<int:id>/students', methods=['GET'])
@token_required
@is_admin
def get_list_student_in_schdedule(id):
    schedule = ScheduleController()
    return schedule.get_student_in_schedule(id)
