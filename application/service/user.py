from application.dao.user import UserDAO
from application.service.auth import generate_password_hash


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_one_user_service(self, uid):
        return self.user_dao.get_one_user_dao(uid)

    def get_all_users_service(self):
        return self.user_dao.get_all_users_dao()

    def get_by_username_service(self, username):
        return self.user_dao.get_by_username_dao(username)

    def create_user_service(self, data):
        data["password"] = generate_password_hash(password=data["password"])
        return self.user_dao.create_user_dao(data)

    def update_user_service(self, data):
        self.user_dao.update_user_dao(data)
        return self.user_dao

    def delete_user_service(self, uid):
        self.user_dao.delete_user_dao(uid)
