import re
from datetime import datetime


class Movie:
    def __init__(self, movie_id: int, title: str, description: str, genre: str):
        """
        initialize the class movie
        :param movie_id: the id of the movie
        :param title: the title of the movie
        :param description: the description of the movie
        :param genre: the genre of the movie
        """
        self.__id = movie_id
        self.__title = title
        self.__description = description
        self.__genre = genre

    @property
    def movie_id(self):
        return self.__id

    @movie_id.setter
    def movie_id(self, new_id):
        self.__id = new_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, new_genre):
        self.__genre = new_genre

    def __str__(self):
        return str(self.movie_id) + "," + str(self.title) + "," + str(self.description) + "," + str(self.genre)


class Client:
    def __init__(self, client_id: int, name: str):
        """
        initialize the class client
        :param client_id: client id
        :param name: name of the client
        """
        self.__client_id = client_id
        self.__name = name

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, new_id):
        self.__client_id = new_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return str(self.client_id) + "," + str(self.name)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.client_id == other.client_id and self.name == other.name
        return False


class Rental:
    def __init__(self, rental_id: int, movie_id: int, client_id: int, rented_date:str, due_date:str, returned_date='1111-11-11'):
        self.__rented_date = rented_date
        self.__rental_id = rental_id
        self.__movie_id = movie_id
        self.__client_id = client_id
        self.__due_date = due_date
        self.__returned_date = returned_date
       

    @property
    def rental_id(self):
        return self.__rental_id

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def client_id(self):
        return self.__client_id

    @property
    def rented_date(self):
        return self.__rented_date

    @property
    def due_date(self):
        return self.__due_date

    @property
    def returned_date(self):
        return self.__returned_date
    @returned_date.setter
    def returned_date(self,date_new):
        self.__returned_date=date_new

    def __str__(self):
        return str(self.rental_id)+','+str(self.movie_id)+','+str(self.client_id)+','+self.rented_date+','+self.due_date+','+self.returned_date