from flask import Blueprint, request

from src.controller.shedule_controller import ScheduleController

schedule = Blueprint(__name__, __name__)


@schedule.route('/schedules', methods=['GET'])
def get_list():
    schedule = ScheduleController()
    return schedule.get_list()


@schedule.route('/schedules', methods=['POST'])
def create():
    data = request.json
    schedule = ScheduleController()
    return schedule.create(data['exam_id'], data['room_id'], data['subject_id'], data['day'], data['start_time'],
                           data['end_time'])
@schedule.route('/schedules/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    schedule = ScheduleController()
    return schedule.update(id,data['exam_id'], data['room_id'], data['subject_id'], data['day'], data['start_time'],
                           data['end_time'])
@schedule.route('/schedules/<int:id>', methods=['DELETE'])
def delete(id):
    schedule = ScheduleController()
    return schedule.delete(id)
