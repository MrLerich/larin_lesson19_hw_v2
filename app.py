from flask import Flask
from flask_restx import Api

from application.views.auth import auth_ns
from application.views.users import user_ns
from config import Config
from setup_db import db
from application.views.directors import director_ns
from application.views.movies import movie_ns
from application.views.genres import genre_ns


def create_app(config: Config) -> Flask: #пркручиваем конфиги
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()  # применяет конфигурацию во все будущие компоненты
    return app

# функция конфигурации приложения
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)




if __name__ == "__main__":
    app = create_app(Config())
    register_extensions(app)
    app.run(host="localhost", port=10001)
