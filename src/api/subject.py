from flask import request, Blueprint

from src.controller.subject_controller import SubjectController

subject = Blueprint(__name__, __name__)
url = '/subjects'
from src.common.authentication import token_required,is_admin

@subject.route(url, methods=['POST'])
@token_required
@is_admin
def create_subject():
    data = request.json
    subject = SubjectController()
    return subject.create(data['name'], data['code'])


@subject.route(url + '/<int:id>', methods=['PUT'])
@token_required
@is_admin
def update_subject(id):
    data = request.json
    subject = SubjectController()
    return subject.update(id, data['name'], data['code'])


@subject.route(url + '/<int:id>', methods=['DELETE'])
@token_required
@is_admin
def delete_subject(id):
    data = request.json
    subject = SubjectController()
    return subject.delete(id)


@subject.route(url, methods=['GET'])
@token_required
@is_admin
def get_subject():
    subject = SubjectController()
    return subject.get_list()
