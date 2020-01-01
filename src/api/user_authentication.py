from flask import request,Blueprint


from src.controller.user_controller import UserController
user_authentication= Blueprint(__name__,__name__)
@user_authentication.route('/authentication',methods=['POST'])
def login():
    data= request.json
    user= UserController()
    return user.login(data['username'],data['password'])
#codethoisinhvien
#nguyentruonggiang08
