from src.domain.domain import *
import copy


class MovieServiceException(Exception):
    def __init__(self, message):
        """
        initialize an error
        :param message: the massage that the error provides
        """
        self.__message = message

    @property
    def message(self):
        return self.__message


class MovieService():
    def __init__(self, repository):
        """
        initialize the movie service
        :param repository: movie_repository
        """
        self._repo = repository
        self.operations = 0
        self._archive = []
        self._archive.append(copy.deepcopy(self._repo.get_all_movie()))

    def add_movie(self, movie: Movie):
        """
        adds a movie to the movie class
        :param movie: an object from class movie
        :return:
        """

        self._repo.ADD_movie(movie)
        self._archive.append(copy.deepcopy(self._repo.get_all_movie()))
        self.operations += 1

    def remove_movie(self, id):
        """
        Remove a movie by id
        :param id: the id of the movie
        :return: All movies
        """
        i = 0
        arr = self.return_all_movie()
        while i < len(arr):
            if arr[i].movie_id == id:
                self._repo.delete_movie(i)
                i -= 1
            i += 1
        self.operations += 1
        self._archive.append(copy.deepcopy(self._repo.get_all_movie()))
        return self._repo.get_all_movie()

    def return_all_movie(self):
        """
        Returns all  movies
        :return: all movies
        """
        return self._repo.get_all_movie()

    def display_movie(self, movie: Movie):
        """
        Displays a movie
        :param movie: a movie
        :return: a movie in string format
        """
        return str(movie) + "\n"

    def update_movie(self, id, title, description, genre):
        """
        It updates a movie
        :param id: new id
        :param title: new title
        :param description: new description
        :param genre: new genre
        """
        i = 0
        arr = self.return_all_movie()
        movie = Movie(id, title, description, genre)
        while i < len(arr):
            if arr[i].movie_id == id:
                self._repo.change_movie(i, movie)

            i += 1
        self.operations += 1
        self._archive.append(copy.deepcopy(self._repo.get_all_movie()))

    def get_by_id(self, id):
        for i in self.return_all_movie():
            if i.movie_id == id:
                return i
        return None
    def partial_name(self,name:str):
        movies = []
        for i in self.return_all_movie():
            if name.casefold() in i.title.casefold():
                movies.append(i)
        return movies

    def partial_id(self,id):
        try:
            id=int(id)
        except:
            raise MovieServiceException("id not an integer")
        movies=[]
        for i in self.return_all_movie():
            if str(id) in str(i.movie_id):
                movies.append(i)
        return movies

    def partial_description(self,description:str):
        movies = []
        for i in self.return_all_movie():
            if description.casefold() in i.description.casefold():
                movies.append(i)
        return movies

    def partial_genre(self,genre:str):
        movies = []
        for i in self.return_all_movie():
            if genre.casefold() in i.genre.casefold():
                movies.append(i)
        return movies