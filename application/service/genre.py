from application.dao.genre import GenreDAO
from application.dao.model.models import Genre


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all_genres_service(self) -> list[Genre]:
        return self.genre_dao.get_all_genres_dao()

    def get_one_genre_service(self, gid: int):
        return self.genre_dao.get_one_genre_dao(gid)

    def create_genre_service(self, genre_d):
        return self.genre_dao.create_genre_dao(genre_d)

    def update_genre_service(self, genre_d):
        self.genre_dao.update_genre_dao(genre_d)
        return self.genre_dao

    def delete_genre_service(self, rid):
        self.genre_dao.delete_genre_dao(rid)

