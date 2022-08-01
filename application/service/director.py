# from application.dao import DirectorDAO
from application.dao.director import DirectorDAO
from application.dao.model.models import Director


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_all_directors_service(self) -> list[Director]:
        return self.director_dao.get_all_directors_dao()

    def get_one_director_service(self, did: int):
        return self.director_dao.get_one_director_dao(did)

    def create_director_service(self, director_d):
        return self.director_dao.create_director_dao(director_d)

    def update_director_service(self, director_d):
        self.director_dao.update_director_dao(director_d)
        return self.director_dao

    def delete_director_service(self, rid):
        self.director_dao.delete_director_dao(rid)


