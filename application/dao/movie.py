# все что касается Movie классы для работы с моделями
from application.dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies_dao(self):
        """ Get all Movies"""
        return self.session.query(Movie).all()

    def get_one_movie_dao(self, mid):
        """Get One Movie by Id"""
        return self.session.query(Movie).filter(Movie.id == mid).one()

    def get_by_director_id_dao(self, did: int):
        """Get Movies by Director Id"""
        movies = self.session.query(Movie)
        return movies.filter(Movie.director_id == did).all()

    def get_by_genre_id_dao(self, gid: int):
        """Get Movies by Genre Id"""
        movies = self.session.query(Movie)
        return movies.filter(Movie.genre_id == gid).all()

    def get_by_year_dao(self, year: int):
        """Get movies by year"""
        movies = self.session.query(Movie)
        return movies.filter(Movie.year == year).all()

    def get_movies_by_many_filters_dao(self, **kwargs):
        """Get Movies by multifilters"""
        movies = self.session.query(Movie)
        return movies.filter_by(**{key: value for key, value in kwargs.items() if value is not None}).all()


    def create_movie_dao(self, **kwargs) -> bool:
        """Create new movie in DB"""
        try:
            self.session.add(Movie(**kwargs))
            self.session.commit()
            return True
        except Exception as e:
            print(f"не удалось добавить фильм\n{e}")
            self.session.rollback()
            return False

    def update_movie_dao(self, data: dict):
        """Get update_movie_service movie"""
        try:
            self.session.query(Movie).filter(Movie.id == data.get("id")).update_user_dao(data)
            self.session.commit()
        except Exception as e:
            print(f"Не удалось обновить фильм\n{e}")
            self.session.rollback()


    def delete_movie_dao(self, mid: int):
        """Delete a movie by id"""
        try:
            self.session.query(Movie).filter(Movie.id == mid).delete_user_dao()
            self.session.commit()
        except Exception as e:
            print(f"Что-то пошло не так, данные не удалены\n{e}")
            self.session.rollback()


