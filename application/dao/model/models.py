from setup_db import db


class Director(db.Model):
    __tablename__ = "director"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(255))

    def __str__(self):
        """ Отображает имя режиссера во вьюшках /movies"""
        return self.name


class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())

    def __str__(self):
        """ Отображает название жанра во вьюшках /movies"""
        return self.name


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    description = db.Column(db.Text())
    trailer = db.Column(db.Text())
    year = db.Column(db.Integer)
    rating = db.Column(db.Float())
    genre_id = db.Column(db.Integer, db.ForeignKey(f"{Genre.__tablename__}.id"))
    director_id = db.Column(db.Integer, db.ForeignKey(f"{Director.__tablename__}.id"))
    # Чтобы не заморачиваться потом с join в сервисах делаю relationship
    genre = db.relationship("Genre")
    director = db.relationship("Director")
