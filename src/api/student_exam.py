from flask import request,Blueprint


from src.controller.student_exam_controller import StudentExamController
student_exam= Blueprint(__name__,__name__)
url='/exams/students'
@student_exam.route(url,methods=['POST'])
def create():
    data=request.json
    student_exam= StudentExamController()
    return student_exam.create(data['exam'],data['code'],data['subject'],data['be_register'])
@student_exam.route(url,methods=['GET'])
def get_list_student_in_exam():
    student_exam = StudentExamController()
    return student_exam.get_list()
