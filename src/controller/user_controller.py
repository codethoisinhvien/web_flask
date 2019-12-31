

from src.model import User


class UserController:
    def login(self, username, password):

        return {"success": True, "token": "12312", "username": "Giang1334", "full_name": "Nguyen duc hai"}

    def create(self, username, password, code, full_name, role):

        try:
            user = User(username=username, password=password, code=code, full_name=full_name, role=role)
            user.save()
            return {"success": True, "message": "Thành công"}
        except Exception as e:
            return {"success": False, "message": "Thất bại"}

    def update(self, id,username, password, code, full_name, role):

        try:
            user = User.get_by_id(id)
            user.username=username
            user.password=password
            user.code=code
            user.full_name=full_name
            user.role=role
            user.save()
            return {"success": True, "message": "Thành công"}
        except Exception as e:
            return {"success": False, "message": "Thất bại"}

    def delete(self, id):
        try:
            user = User.get(User.id);
            user.delete()
            return {"success": True, "message": "Thành công"}
        except Exception as e:
            return {"success": False, "message": "Thất bại",}

    def get_list(self):
        user = User()
        list_user = user.select().dicts().execute()
        data = []
        for i in list_user:
            data.append(i)
        print(list_user)
        return {"success": True, "users": data}
