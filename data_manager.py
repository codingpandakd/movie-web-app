import os
from models import db, User, Movie
import requests

OMDB_API_KEY = os.getenv('OMDB_API_KEY')
OMDB_URL = 'http://www.omdbapi.com/'


class DataManager:
    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_users(self):
        return User.query.all()

    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, user_id, movie_title):
        # Fetch movie info from OMDb
        if not OMDB_API_KEY:
            raise RuntimeError("OMDB_API_KEY not set!")
        params = {'apikey': OMDB_API_KEY, 't': movie_title}
        r = requests.get(OMDB_URL, params=params)
        data = r.json()
        if data.get('Response') == 'True':
            movie = Movie(
                title=data.get('Title'),
                director=data.get('Director'),
                year=data.get('Year'),
                poster_url=data.get('Poster'),
                user_id=user_id
            )
            db.session.add(movie)
            db.session.commit()
            return True
        return False

    def update_movie(self, movie_id, new_title):
        movie = Movie.query.get(movie_id)
        if movie:
            movie.title = new_title
            db.session.commit()

    def delete_movie(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            db.session.delete(movie)
            db.session.commit()

