from application.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one_user_dao(self, uid):
        return self.session.query(User).get(uid)

    def get_all_users_dao(self):
        return self.session.query(User).all()

    def get_by_username_dao(self, username):
        return self.session.query(User).filter(User.username == username).one()

    def create_user_dao(self, data):
        ent = User(**data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete_user_dao(self, uid):
        user = self.get_one_user_dao(uid)
        self.session.delete_user(user)
        self.session.commit()

    def update_user_dao(self, data):
        user = self.get_one_user_dao(data.get("id"))
        if data.get("name"):
            user.name = data.get("name")
        if data.get("role"):
            user.role = data.get("role")
        if data.get("password"):
            user.password = data.get("password")
        self.session.add(user)
        self.session.commit()


