from flask import request,Blueprint


from src.controller.user_controller import UserController
user= Blueprint(__name__,__name__)
@user.route('/users',methods=['POST'])
def create():
    data=request.json
    user= UserController()
    return user.create(data['username'],data['password'],data['code'],data['full_name'],1)
@user.route('/users',methods=['GET'])
def get_list_user():
    request.data
    user= UserController()
    return user.get_list();
@user.route('/users/<int:id>',methods=['DELETE'])
def delete_user(id):
    user= UserController()
    return user.delete(id);
@user.route('/users/<int:id>',methods=['PUT'])
def update_user(id):
    data = request.json
    user= UserController()
    return user.update(id,data['username'],data['password'],data['code'],data['full_name'],data['role']);

