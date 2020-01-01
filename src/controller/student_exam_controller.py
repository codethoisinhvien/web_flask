import uuid

from src.model import UserExamSubject, Exam, User, Subject


class StudentExamController:

    def create(self, exam_name, code, subject_code, be_register):
        try:
            exam = Exam.get(Exam.name == exam_name)
            user = User.get(User.code == code)
            subject = Subject.get(Subject.code == subject_code)
            user_exam_subject = UserExamSubject.create(user_id=user.id, exam_id=exam.id, subject_id=subject.id,
                                                       be_register=be_register, status=True, id=uuid.uuid4())
            user_exam_subject.save()
            return {"success": True, "message": "Thành công",}
        except Exception as e:
            print(e)
            return {"success": False, "message": "Thất bại"}

    def get_list(self):
        user_exam_subject = UserExamSubject()
        datas = user_exam_subject.get_list()
        data = []
        for i in datas:
            data.append(i)
        return {"success": True, "data": data}

    def delele(self, id):
        try:
            user_exam_subject = UserExamSubject.get(UserExamSubject.id == id)
            user_exam_subject.delete()
            return {"success": True, "message": "Thành công"}
        except Exception as e:
            return {"success": False, "message": "Thất bại"}
