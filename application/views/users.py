from flask import request
from flask_restx import Namespace, Resource

from application.dao.model.user import UserSchema
from implemented import user_service

user_ns: Namespace = Namespace('users')

@user_ns.route('/')
class UserView(Resource):
    def post(self):
        data = request.json
        return UserSchema().dump(user_service.create_user_service(data)), 201
