from src.domain.domain import *
import copy



class MovieException(Exception):
    def __init__(self, message):
        """
        initialize an error
        :param message: the massage that the error provides
        """
        self.__message = message

    @property
    def message(self):
        return self.__message




class MovieRepo():
    def __init__(self,file_name):
        """
        initialize the movie repo class
        :param file_name: file name
        """
        self._data_movie=[]
        self._file_name = file_name
        try:
            self._load_file()
        except:
            pass

    def _load_file(self):
        """
        it loads the data from the file into fin
        :return:
        """
        try :
            fin = open(self._file_name, 'rt')
        except FileNotFoundError as e:
            raise e

        line=fin.readline().strip()

        while line!="":
            line=line.split(",")
            self._data_movie.append(Movie(int(line[0]), line[1], line[2], line[3]))
            line=fin.readline().strip()
        fin.close()

    def _save__file(self):
        """
        saves the date into the file
        :return:
        """
        fout=open(self._file_name,'wt')
        for obj in self.get_all_movie() :
            fout.write("{},{},{},{}".format(obj.movie_id,obj.title,obj.description,obj.genre))
            fout.write("\n")
        fout.close()

    def ADD_movie(self, movie:Movie):
        """
        adds a movie to the movie class
        :param movie: an object from movie class
        :return:
        """

        for i in self._data_movie:
            if movie.movie_id==i.movie_id or movie.title==i.title:
                raise MovieException("movie id already added")
        self._data_movie.append(movie)
        self._save__file()

    def delete_movie(self, movie):
        """
        delets the movie object from the movie class
        :param movie: the position on which we find the object we want to delete
        :return:
        """
        self._data_movie.pop(movie)
        self._save__file()

    def get_all_movie(self):
        """
        returns the list with all the objects type movie
        :return:
        """
        return self._data_movie
    def change_data_movie(self, new_lst):
        """
        we use this function for the undo command
        :param new_lst:
        :return:
        """
        self._data_movie = copy.deepcopy(new_lst)
        self._save__file()
    def change_movie(self, i, movie):
        """change the data of an movie object"""
        self._data_movie[i]=movie
        self._save__file()