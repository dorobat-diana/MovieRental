from src.services.movie_service import *
from src.services.rental_service import *
from src.services.client_service import *


class UserInterfaceException(Exception):

    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message

class UserInterface():
    def __init__(self, serv1,serv2,serv3):
        self._service_movie = serv1
        self._service_client = serv2
        self._service_rental= serv3
    def menu(self):

        while True:
            print("1.Manage clients")
            print("2.Manage movies")
            print("3.Rent a movie")
            print("4.Search for movies")
            print("5.Search for clients")
            print("6.Statistics")
            print("7.Return a movie")
            print("0.Exit program")


            print("\n")
            token = input("Select a command>>>")
            if token=="2" :
                while True :
                    print("1.Add movie")
                    print("2.Remove movie")
                    print("3.Update movie")
                    print("4.List all movies")
                    print("0.Exit section movies")
                    token_1= input("Select a command>>>")
                    if token_1=="1" :
                        id=input("id>>>")
                        title=input("title>>>")
                        description=input("description>>>")
                        genre=input("genre>>>")
                        try :
                            self._service_movie.add_movie(Movie(int(id), title, description, genre))
                        except Exception as e:
                            print(e)

                    elif token_1=="2" :
                        id = input("id>>>")

                        try:
                            id=int(id)
                        except:
                            print("id not an integer")
                        else :
                            self._service_movie.remove_movie(id)

                    elif token_1=="3":
                        old_id=input("id>>>")

                        title=input("new title>>>")
                        description=input("new description>>>")
                        genre=input("new genre>>>")
                        try:

                            old_id=int(old_id)
                        except:
                            print("id not an integer")
                        self._service_movie.update_movie(old_id, title, description, genre)
                    elif token_1=="4":
                        for i in self._service_movie.return_all_movie():
                            print(self._service_movie.display_movie(i))
                    elif token_1=="0":
                        break
            elif token=="1":
                while True :
                    print("1.Add client")
                    print("2.Remove client")
                    print("3.Update client")
                    print("4.List all clients")
                    print("0.Exit section clients")
                    token_1= input("Select a command>>>")
                    if token_1=="1" :
                        id=input("id>>>")
                        name=input("name>>>")
                        try :
                            self._service_client.add_client(Client(int(id), name))
                        except Exception as e:
                            print(e)

                    elif token_1=="2" :
                        id = input("id>>>")

                        try:
                            id=int(id)
                        except:
                            print("id not an integer")
                        else :
                            self._service_client.remove_client(id)

                    elif token_1=="3":
                        old_id=input("id>>>")

                        name=input("name>>>")
                        try:

                            old_id=int(old_id)
                        except:
                            print("id not an integer")
                        self._service_client.update_client(old_id, name)
                    elif token_1=="4":
                        for i in self._service_client.return_all_client():
                            print(self._service_client.display_client(i))
                    elif token_1=="0":
                        break
            elif token=="3":
                rental_id=input("rental_id>>>")
                movie_id = input('movie_id>>>')
                client_id=input("client_id>>>")
                rented_date=input("rented_date>>>")
                due_date=input("due_date>>>")
                try:
                    if self._service_client.get_by_id(int(client_id)) is not None and self._service_movie.get_by_id(int(movie_id)) is not None:
                        self._service_rental.add_rental(Rental(int(rental_id), int(movie_id), int(client_id), rented_date, due_date))
                    else :
                        print("the movie or the client doesn't exist")
                except Exception as e:
                    print(e)
            elif token=='4':
                print("Please select how you want to search the movie")
                print("1. By name")
                print("2. By id")
                print("3. By description")
                print("4. By genre")
                method=input(">>>")
                if method=="1":
                    print("Please introduce the name of the movie:")
                    name=input(">>>")
                    list=[]
                    list=self._service_movie.partial_name(name)
                    for i in list:
                        print(self._service_movie.display_movie(i))
                elif method=="2":
                    print("Please introduce the id of the movie:")
                    id=input(">>>")
                    list=[]
                    try:
                        list=self._service_movie.partial_id(id)
                        for i in list:
                            print(self._service_movie.display_movie(i))
                    except Exception as e:
                        print(e)
                elif method=="3":
                    print("Please introduce the description of the movie:")
                    description=input(">>>")
                    list=[]
                    list=self._service_movie.partial_description(description)
                    for i in list:
                        print(self._service_movie.display_movie(i))
                elif method=="4":
                    print("Please introduce the genre of the movie:")
                    genre=input(">>>")
                    list=[]
                    list=self._service_movie.partial_genre(genre)
                    for i in list:
                        print(self._service_movie.display_movie(i))
                else:
                    print("The selected method isn't valid")
            elif token=="5":
                print("Please select how you want to search the client: ")
                print("1. By name")
                print("2. By id")
                method=input(">>>")
                if method=="1":
                    print("Please introduce the name of the client:")
                    name=input(">>>")
                    list=[]
                    list=self._service_client.partial_name(name)
                    for i  in list:
                        print(self._service_client.display_client(i))
                elif method=="2":
                    print("Please introduce the nid of the client:")
                    id=input(">>>")
                    list=[]
                    try:
                        list=self._service_client.partial_id(id)
                        for i in list:
                            print(self._service_client.display_client(i))
                    except Exception as e:
                        print(e)
                else:
                    print("The selected method isn't valid")
            elif token=="6":
                print("Please select which statistics you want to see")
                print("1.Most rented movies")
                print("2.Most active clients")
                print("3.Late rentals")
                stat=input(">>>")
                if stat=="3":
                    list=self._service_rental.late_rental()
                    for i in list:
                        print(self._service_rental.display_rental(i))
                elif stat=="1":

                    list=self._service_rental.movie_top(self._service_movie.return_all_movie())
                    for i in list:
                        print(self._service_movie.display_movie(i))
                elif stat=="2":
                    list=self._service_rental.client_top(self._service_client.return_all_client())
                    for i in list:
                        print(self._service_movie.display_movie(i))
                else:
                    print("The selected method isn't valid")
            elif token=="7":
                print("Please introduce the rental id and the date of the return:")
                id=input("id>>>")
                date=input("date>>>")
                try:
                    self._service_rental.return_movie(id,date)
                except Exception as e:
                    print(e)
            elif token=="0":
                break
            else:
                print("The selected method isn't valid")
