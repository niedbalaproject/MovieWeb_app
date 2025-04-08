import json
from MovieWeb_app.data_manager.data_manager_interface import DataManagerInterface


class JSONDataManager(DataManagerInterface):
    def __init__(self, filename='movies.json'):
        self.filename = filename
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file."""
        with open(self.filename, 'r') as handle:
            self.data = json.load(handle)

    def _save_data(self):
        """Writes the current data back to the JSON file."""
        with open(self.filename, 'w') as handle:
            json.dump(self.data, handle, indent=2)

    def get_all_users(self):
        """Returns all users from the JSON file."""
        return self.data

    def get_user_movies(self, user_id):
        """Returns the list of movies for the given user."""
        user = self._find_user(user_id)
        return user['movies'] if user else []

    def add_movie(self, user_id, movie_data):
        user = self._find_user(user_id)
        if user:
            movie_data['id'] = self._get_next_movie_id(user)
            user['movies'].append(movie_data)
            self._save_data()
            return True
        return False

    def update_movie(self, user_id, movie_id, updated_data):
        user = self._find_user(user_id)
        if user:
            for movie in user['movies']:
                if movie['id'] == movie_id:
                    movie.update(updated_data)
                    self._save_data()
                    return True
        return False

    def delete_movie(self, user_id, movie_id):
        user = self._find_user(user_id)
        if user:
            user['movies'] = [movie for movie in user['movies'] if movie['id'] != movie_id]
            self._save_data()
            return True
        return False

    def _find_user(self, user_id):
        return next((user for user in self.data if user['id' == user_id]), None)

    def _get_next_movie_id(self, user):
        if not user['movies']:
            return 1
        return max(movie['id'] for movie in user['movies']) + 1
