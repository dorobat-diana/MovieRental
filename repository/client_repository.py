from src.domain.domain import *
import copy


class ClientException(Exception):
    def __init__(self, message):
        """
        initialize an error
        :param message: the massage that the error provides
        """
        self.__message = message

    @property
    def message(self):
        return self.__message


class ClientRepo():
    def __init__(self, file_name):
        """
        initialize the client repo class
        :param file_name: file name
        """
        self._data_client = []
        self._file_name = file_name
        try:
            self._load_file()
        except:
            pass

    def _load_file(self):
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
            self._data_client.append(Client(int(line[0]), line[1]))
            line = fin.readline().strip()
        fin.close()

    def _save__file(self):
        """
        saves the data into the file
        :return:
        """
        fout = open(self._file_name, 'wt')
        for obj in self.get_all_client():
            fout.write("{},{}".format(obj.client_id, obj.name))
            fout.write("\n")
        fout.close()

    def ADD_client(self, client: Client):
        """
        adds a client to the class
        :param client: the object client from the class client
        :return:
        """

        for i in self._data_client:
            if client.client_id == i.client_id:
                raise ClientException("client id already added")
        self._data_client.append(client)
        self._save__file()

    def delete_client(self, i):
        """
        deletes a client from the class
        :param i: the position where we find the client we want to remove
        :return:
        """
        self._data_client.pop(i)
        self._save__file()

    def get_all_client(self):
        """returns the list with all the clients"""
        return self._data_client

    def change_data_client(self, new_lst):
        """we use this function for the undo method"""
        self._data_client = copy.deepcopy(new_lst)
        self._save__file()

    def change_client(self, i, client):
        """changes the data of a client """
        self._data_client[i] = client
        self._save__file()
