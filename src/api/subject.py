from flask import request, Blueprint

from src.controller.subject_controller import SubjectController

subject = Blueprint(__name__, __name__)
url = '/subjects'


@subject.route(url, methods=['POST'])
def create_subject():
    data = request.json
    subject = SubjectController()
    return subject.create(data['name'], data['code'])


@subject.route(url + '/<int:id>', methods=['PUT'])
def update_subject(id):
    data = request.json
    subject = SubjectController()
    return subject.update(id, data['name'], data['code'])


@subject.route(url + '/<int:id>', methods=['DELETE'])
def delete_subject(id):
    data = request.json
    subject = SubjectController()
    return subject.delete(id)


@subject.route(url, methods=['GET'])
def get_subject():
    subject = SubjectController()
    return subject.get_list()
