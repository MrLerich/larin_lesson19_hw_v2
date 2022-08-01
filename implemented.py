from application.dao.director import DirectorDAO
from application.dao.genre import GenreDAO
from application.dao.movie import MovieDAO
from application.dao.user import UserDAO
from application.service.director import DirectorService
from application.service.user import UserService
from setup_db import db
from application.service.movie import MovieService
from application.service.genre import GenreService

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao=movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao=genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao=director_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao=user_dao)
