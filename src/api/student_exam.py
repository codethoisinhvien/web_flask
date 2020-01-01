from flask import request,Blueprint

from src.common.authentication import token_required,is_admin
from src.controller.student_exam_controller import StudentExamController
student_exam= Blueprint(__name__,__name__)
url='/exams/students'
@student_exam.route(url,methods=['POST'])
@token_required
@is_admin
def create():
    data=request.json
    student_exam= StudentExamController()
    return student_exam.create(data['exam'],data['code'],data['subject'],data['be_register'])
@student_exam.route(url,methods=['GET'])
@token_required
@is_admin
def get_list_student_in_exam():
    student_exam = StudentExamController()
    return student_exam.get_list()
