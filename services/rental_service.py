
from src.domain.domain import *

from datetime import datetime
import copy

from datetime import date


import re



class RentalServiceException(Exception):
    def __init__(self, message):
        """initialize an error
        :param message: the massage that the error provides"""
        self.__message = message

    @property
    def message(self):
        return self.__message





class RentalService():
    def __init__(self, repository):

        self._repo = repository
        self.operations = 0
        self._archive = []
        self._archive.append(copy.deepcopy(self._repo.get_all_rental()))

    def add_rental(self, rental: Rental):

        self._repo.ADD_rental(rental)
        self._archive.append(copy.deepcopy(self._repo.get_all_rental()))
        self.operations += 1

    def return_all(self):
        return self._repo.get_all_rental()

    def late_rental(self):
        late=[]
        for rental in self._repo.get_all_rental():
            if datetime.strptime(rental.due_date ,'%Y-%m-%d').date()<date.today() and rental.returned_date=="1111-11-11":
                late.append(rental)
        late= self.sort_rental(late)
        return late


    def sort_rental(self,rentals):
        observator=1
        while observator==1:
            observator=0
            for pos in range (0,len(rentals)-1):
                second=datetime.strptime(rentals[pos+1].due_date,'%Y-%m-%d')
                first=datetime.strptime(rentals[pos].due_date,'%Y-%m-%d')
                today=datetime.today()
                print(today-second,today-first)
                if today-second>today-first :
                    observator=1
                    switch=rentals[pos+1]
                    rentals[pos+1]=rentals[pos]
                    rentals[pos]=switch
        return rentals
    def display_rental(self,rental:Rental):
        return str(rental)+"\n"
    def movie_top(self,list):
        observator=1
        while observator==1:
            observator=0
            for mov in range(0,len(list)-1):
                first=self.days_of_rent_movie(list[mov])
                second=self.days_of_rent_movie(list[mov + 1])
                if second>first:
                    observator=1
                    switch=list[mov]
                    list[mov]=list[mov+1]
                    list[mov+1]=switch
        return list
    def days_of_rent_movie(self, movie:Movie):
        list=self.return_all()
        sum=0
        for i in list:
            if i.movie_id==movie.movie_id:
                if i.returned_date=="1111-11-11":
                    today=datetime.today()
                    rented=datetime.strptime(i.rented_date,'%Y-%m-%d')
                    delta=today-rented
                    delta=abs(delta.days)
                    sum+=delta
                else:
                    returned=datetime.strptime(i.returned_date,'%Y-%m-%d')
                    rented = datetime.strptime(i.rented_date, '%Y-%m-%d')
                    delta=returned-rented
                    delta=abs(delta.days)
                    sum+=delta
        return sum
    def client_top(self,list):
        observator=1
        while observator==1:
            observator=0
            for pos in range(0,len(list)-1):
                first=self.days_of_rent_client(list[pos])
                second=self.days_of_rent_client(list[pos+1])
                if first<second:
                    switch=list[pos]
                    list[pos]=list[pos+1]
                    list[pos+1]=switch
                    observator=1
        return list

    def days_of_rent_client(self,client:Client):
        list = self.return_all()
        sum = 0
        for i in list:
            if i.client_id == client.client_id:
                if i.returned_date == "1111-11-11":
                    today = datetime.today()
                    rented = datetime.strptime(i.rented_date, '%Y-%m-%d')
                    delta = today - rented
                    delta = abs(delta.days)
                    sum += delta
                else:
                    returned = datetime.strptime(i.returned_date, '%Y-%m-%d')
                    rented = datetime.strptime(i.rented_date, '%Y-%m-%d')
                    delta = returned - rented
                    delta = abs(delta.days)
                    sum += delta
        return sum
    def return_movie(self,id,date):
        list=self.return_all()
        for rental in list:
            rent=str(rental.rental_id)
            if id==rent:
                self._repo.Return_movie(rental,date)

