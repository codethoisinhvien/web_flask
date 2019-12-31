from src.model import Exam


class ExamController:

    def create(self, name, status):

        try:
            exam = Exam(name=name, status=status)
            exam.save()
            return {"success": True, "message": "Thành công", "exam_id": exam.id}
        except Exception as e:
            return {"success": False, "message": "Thất bại"}

    def update(self, id, name, status):

        try:
            exam = Exam.get_by_id(id)
            exam.name = name
            exam.status = status
            exam.save()
            return {"success": True, "message": "Thành công", "exam_id": exam.id}
        except Exception as e:
            return {"success": False, "message": "Thất bại"}

    def delete(self, id):
        try:
            exam = Exam.get_by_id(id);
            exam.delete()
            return {"success": True, "message": "Thành công"}
        except Exception as e:
            return {"success": False, "message": "Thất bại"}

    def get_list(self):
        exam = Exam()
        exams = exam.select().dicts().execute()
        data = []
        for i in exams:
            data.append(i)
        return {"success": True, "exams": data}
