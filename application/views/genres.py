from flask import request
from flask_restx import Resource, Namespace
from sqlalchemy.exc import NoResultFound


from application.dao.model.schema import GenreSchema
from application.service.decorators import auth_required, admin_required
from implemented import genre_service

genre_ns = Namespace("genres")
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):
    """Получить все жанры"""
    @auth_required
    def get(self):
        genres = genre_service.get_all_genres_service()
        return genres_schema.dump(genres), 200

    @admin_required
    def post(self):
        data = request.json
        return GenreSchema().dump(genre_service.create(data)), 201

@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    """Получить все жанры по id"""

    @auth_required
    def get(self, gid: int):
        try:
            genre = genre_service.get_one_genre_service(gid)
        except NoResultFound as e:
            return f"{e}", 400
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, gid):
        data = request.json
        if not data.get("id") or (data.get("id") != gid):
            data["id"] = gid

    @admin_required
    def delete(self, gid):
        return genre_service.delete_genre_service(gid), 200
