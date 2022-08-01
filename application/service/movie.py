from application.dao.model.models import Movie
from application.dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all_movies_service(self) -> list[Movie]:
        return self.movie_dao.get_all_movies_dao()

    def get_one_movie_service(self, mid: int):
        return self.movie_dao.get_one_movie_dao(mid)

    def get_by_director_id_service(self, director_id: int):
        return self.movie_dao.get_by_director_id_dao(director_id)

    def get_by_genre_id_service(self, genre_id: int):
        return self.movie_dao.get_by_genre_id_dao(genre_id)

    def get_by_year_service(self, year: int):
        return self.movie_dao.get_by_year_dao(year)

    def get_movies_by_many_filters_service(self, **kwargs):
        """Универсальный поиск по нескольким параметрам """
        return self.movie_dao.get_movies_by_many_filters_dao(**kwargs)

    def create_movie_service(self, kwargs):
        return self.movie_dao.create_movie_dao(**kwargs)

    def update_movie_service(self, data: dict):
        self.movie_dao.update_movie_dao(data)


    def delete_movie_service(self, mid: int):
        self.movie_dao.delete_movie_dao(mid)
