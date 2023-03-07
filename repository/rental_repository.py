from src.domain.domain import *
from src.repository.client_repository import *
from src.repository.movie_repository import *


import re
from datetime import datetime
import copy

from datetime import date



class RentalException(Exception):
    def __init__(self, message):
        """
        initialize an error
        :param message: the massage that the error provides
        """
        self.__message = message

    @property
    def message(self):
        return self.__message

class RentalRepo ():
    def __init__(self,file_name):
        """
                initialize the client repo class
                :param file_name: file name
                """
        self._data_rental = []
        self._file_name = file_name
        try:
            self.__load_file()
        except:
            pass

    def __load_file(self):
        """
        loads the data from the file into fin
        :return:
        """
        try:
            fin = open(self._file_name, 'rt')
        except FileNotFoundError as e:
            raise e

        line = fin.readline().strip()

        while line != "":
            line = line.split(",")
            self._data_rental.append(Rental(int(line[0]), int(line[1]),int(line[2]),line[3],line[4],line[5]))
            line = fin.readline().strip()
        fin.close()

    def _save__file(self):
        """
        saves the data into the file
        :return:
        """
        fout = open(self._file_name, 'wt')
        for obj in self.get_all_rental():
            fout.write("{},{},{},{},{},{}".format(obj.rental_id, obj.movie_id,obj.client_id,obj.rented_date,obj.due_date,obj.returned_date))
            fout.write("\n")
        fout.close()

    def get_all_rental(self):
        return self._data_rental

    def ADD_rental(self,rental:Rental):
        pattern = '....-..-..'
        if re.fullmatch(pattern,rental.due_date) is not None and re.fullmatch(pattern,rental.rented_date) is not None :
            for i in self._data_rental:
                if rental.rental_id==i.rental_id :
                    raise RentalException("id already added")
                if rental.client_id==i.client_id :
                    due=i.due_date
                    rented=i.rented_date
                    if datetime.strptime(due ,'%Y-%m-%d').date()<date.today() and i.returned_date=="1111-11-11" and  re.fullmatch(pattern,due) is not None :
                        raise RentalException("Client has passed their due date on another rental")
                    elif re.fullmatch(pattern,due) is None or re.fullmatch(pattern,rented) is None:
                        raise RentalException("Date not valid")
            self._data_rental.append(rental)
            self._save__file()
        else:
            raise RentalException("Date not valid")
    def Return_movie(self,rental:Rental,date):
        pattern = '....-..-..'
        if re.fullmatch(pattern,date) is None:
            raise RentalException("Date not valid")
        elif rental.returned_date != '1111-11-11':
            raise RentalException("Movie already returned")
        else:
            rental.returned_date=date
            self._save__file()



