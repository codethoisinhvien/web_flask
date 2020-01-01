

from src.model import User

from src.common.authentication import authenticate,create_token
class UserController:
    def login(self, username, password):
        user = authenticate(username,password)
        if user is not None:
            print(user)
            return {"success":True,"token":create_token({"id":user.id,"username":user.username,"role":user.role}),"username":user.username,"full_name":user.full_name,"code":user.code}
        return {"success": False, "message":"Mật khẩu hoặc tài khoản không đúng"}

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
