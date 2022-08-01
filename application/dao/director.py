# все что касается Director методов
from application.dao.model.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors_dao(self):
        return self.session.query(Director).all()

    def get_one_director_dao(self, did):
        return self.session.query(Director).filter(Director.id == did).one()

    def create_director_dao(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete_director_dao(self, rid):
        director = self.get_one_director_dao(rid)
        self.session.delete(director)
        self.session.commit()

    def update_director_dao(self, director_d):
        director = self.get_one_director_dao(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()