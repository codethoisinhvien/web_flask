from flask import request,Blueprint


from src.controller.user_controller import UserController
user_authentication= Blueprint(__name__,__name__)
@user_authentication.route('/authentication',methods=['POST'])
def login():
    user= UserController()
    return user.login("12312","sdasd")
