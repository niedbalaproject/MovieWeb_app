from abc import ABC, abstractmethod


class DataManagerInterface(ABC):

    @abstractmethod
    def get_all_users(self):
        """
        A list of all users, where each user is a dictionary with keys like 'id', 'name', and 'movies'.
        :return: list[dict]
        """
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        """
        A list of the user's favorite movies, where each movie is a dictionary with movie details.
        :param user_id: id of a user (int)
        :return: list[dict]
        """
        pass
