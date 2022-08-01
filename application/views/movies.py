from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound

from application.dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns: Namespace = Namespace("movies")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):

    def get(self):
        """Универсальный поиск фильмов по нескольким параметрам"""
        if len(request.args) > 0:
        #если что-то подали,то ищем по id,нет: выдаем все
            return movies_schema.dump(movie_service.get_movies_by_many_filters_service(
                **request.args

            )
            )
        else:
            return movies_schema.dump(movie_service.get_all_movies_service()), 200

    def post(self):
        """Добавление нового фильма"""
        data = request.json
        if movie_service.create_movie_service(data):
            return "Успешно добавлено", 201
        else:
            return "Запись не добавлена", 503


@movie_ns.route("/<int:mid>")
class MovieView(Resource):

    def get(self, mid: int):
        try:
            movie = movie_service.get_one_movie_service(mid)
        except NoResultFound as e:
            return f"{e}", 400
        return movie_schema.dump(movie), 200

    def put(self, mid: int):
        """Обновление инфы по фильму"""
        movie_service.update_movie_service(request.json)
        return "Успешно обновлено", 201

    def delete(self, mid: int):
        """Удаление фильма"""
        movie_service.delete_movie_service(mid)
        return "Успешно удалено", 204
