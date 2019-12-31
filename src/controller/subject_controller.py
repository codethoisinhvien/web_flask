
from src.model import Subject


class SubjectController:

    def create(self,name,code):

        try:
            subject  = Subject(name=name,code=code)
            subject.save()
            return {"success": True, "message": "Thành công","subject_id":subject.id}
        except Exception as e:
            return {"success": False, "message": "Thất bại"}

    def update(self, id,name,code):

        try:
            subject = Subject.get_by_id(id)
            subject.name=name
            subject.code= code
            subject.save()
            return {"success": True, "message": "Thành công"}
        except Exception as e:
            return {"success": False, "message": "Thất bại"}

    def delete(self, id):
        try:
            subject = Subject.get_by_id(id);
            subject.delete()
            return {"success": True, "message": "Thành công"}
        except Exception as e:
            print(e)
            return {"success": False, "message": "Thất bại"}

    def get_list(self):
        subject = Subject()
        subjects = subject.select().dicts().execute()
        data = []
        for i in subjects:
            data.append(i)
        return {"success": True, "subjects": data}
