# все что касается Genre методов
from application.dao.model.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres_dao(self):
        return self.session.query(Genre).all()

    def get_one_genre_dao(self, gid):
        return self.session.query(Genre).get(gid)

    def create_genre_dao(self, genre_d):
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete_genre_dao(self, gid):
        genre = self.get_one_genre_dao(gid)
        self.session.delete(genre)
        self.session.commit()

    def update_genre_dao(self, genre_d):
        genre = self.get_one_genre_dao(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()
