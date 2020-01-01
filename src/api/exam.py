from flask import request, Blueprint

from src.controller.exam_controller import ExamController

exam = Blueprint(__name__, __name__)
url = '/exams'
from src.common.authentication import token_required,is_admin

@exam.route(url, methods=['POST'])
@token_required
@is_admin
def create_subject():
    data = request.json
    exam = ExamController()
    return exam.create(data['name'], data['status'])


@exam.route(url + '/<int:id>', methods=['PUT'])
@token_required
@is_admin
def update_subject(id):
    data = request.json
    exam = ExamController()
    return exam.update(id, data['name'], data['status'])


@exam.route(url + '/<int:id>', methods=['DELETE'])
@token_required
@is_admin
def delete_subject(id):
    data = request.json
    exam = ExamController()
    return exam.delete(id)


@exam.route(url , methods=['GET'])
@token_required
@is_admin
def get_subject():
    exam = ExamController()
    return exam.get_list()
