from flask import request, Blueprint

from src.controller.exam_controller import ExamController

exam = Blueprint(__name__, __name__)
url = '/exams'


@exam.route(url, methods=['POST'])
def create_subject():
    data = request.json
    exam = ExamController()
    return exam.create(data['name'], data['status'])


@exam.route(url + '/<int:id>', methods=['PUT'])
def update_subject(id):
    data = request.json
    exam = ExamController()
    return exam.update(id, data['name'], data['status'])


@exam.route(url + '/<int:id>', methods=['DELETE'])
def delete_subject(id):
    data = request.json
    exam = ExamController()
    return exam.delete(id)


@exam.route(url , methods=['GET'])
def get_subject():
    exam = ExamController()
    return exam.get_list()
