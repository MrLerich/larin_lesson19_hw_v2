from flask import request
from flask_restx import Resource, Namespace
from sqlalchemy.exc import NoResultFound

from application.dao.model.schema import DirectorSchema
from application.service.decorators import auth_required, admin_required
from implemented import director_service

director_ns = Namespace("directors")
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route("/")
class DirectorsView(Resource):
    @auth_required
    def get(self):
        directors = director_service.get_all_directors_service()
        return directors_schema.dump(directors), 200

    @admin_required
    def post(self):
        data = request.json
        return DirectorSchema().dump(director_service.create(data)), 201


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    @auth_required
    def get(self, did: int):
        try:
            director = director_service.get_one_director_service(did)
        except NoResultFound as e:
            return f"{e}", 400
        return director_schema.dump(director), 200

    @admin_required
    def put(self, did):
        data = request.json
        if not data.get("id") or (data.get("id") != did):
            data["id"] = did

    @admin_required
    def delete(self, did):
        return director_service.delete_director_service(did), 200
