from src.domain.domain import *
import copy


class ClientServiceException(Exception):
    def __init__(self, message):
        """initialize an error
        :param message: the massage that the error provides"""
        self.__message = message

    @property
    def message(self):
        return self.__message


class ClientService():
    def __init__(self, repository):
        """
        Initialize the Client Service
        :param repository: repository
        """
        self._repo = repository
        self.operations = 0
        self._archive = []
        self._archive.append(copy.deepcopy(self._repo.get_all_client()))

    def add_client(self, client: Client):
        """
        Adds a client
        :param client:Client
        """
        self._repo.ADD_client(client)
        self._archive.append(copy.deepcopy(self._repo.get_all_client()))
        self.operations += 1

    def remove_client(self, id):
        """
        Removes a Client
        :param id: id of the client
        :return: All Clients
        """
        i = 0
        arr = self.return_all_client()
        while i < len(arr):
            if arr[i].client_id == id:
                self._repo.delete_client(i)
                i -= 1
            i += 1
        self.operations += 1
        self._archive.append(copy.deepcopy(self._repo.get_all_client()))
        return self._repo.get_all_client()

    def return_all_client(self):
        """
        Returns all the clients
        :return: all clients
        """
        return self._repo.get_all_client()

    def display_client(self, client: Client):
        """
        Displays a client in a string format
        :param client: Client
        :return: a client in a string format
        """
        return str(client) + "\n"

    def update_client(self, id, name):
        """
        It updates a client
        :param id: new id
        :param name: new name
        """
        i = 0
        arr = self.return_all_client()
        client = Client(int(id), name)
        while i < len(arr):
            if arr[i].client_id == id:
                self._repo.change_client(i, client)

            i += 1
        self.operations += 1
        self._archive.append(copy.deepcopy(self._repo.get_all_client()))

    def get_by_id(self,id):
        for i in self.return_all_client() :
            if i.client_id==id :
                return i
        return None

    def partial_name(self,name:str):
        clients=[]
        for i in self.return_all_client():
            if name.casefold() in i.name.casefold() :
                clients.append(i)
        return clients
    def partial_id(self,id):
        try:
            id=int(id)
        except:
            raise ClientServiceException("id not an integer")
        clients=[]
        for i in self.return_all_client():
            if str(id) in str(i.client_id):
                clients.append(i)
        return clients


