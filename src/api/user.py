from flask import request,Blueprint


from src.controller.user_controller import UserController
user= Blueprint(__name__,__name__)

from src.common.authentication import token_required,is_admin
@user.route('/users',methods=['POST'])
@token_required
@is_admin
def create():
    data=request.json
    user= UserController()
    return user.create(data['username'],data['password'],data['code'],data['full_name'],1)
@user.route('/users',methods=['GET'])
@token_required
@is_admin
def get_list_user():
    request.data
    user= UserController()
    return user.get_list();
@token_required
@is_admin
@user.route('/users/<int:id>',methods=['DELETE'])
def delete_user(id):
    user= UserController()
    return user.delete(id);

@user.route('/users/<int:id>',methods=['PUT'])
@token_required
@is_admin
def update_user(id):
    data = request.json
    user= UserController()
    return user.update(id,data['username'],data['password'],data['code'],data['full_name'],data['role']);

