from unittest import TestCase
import unittest
from src.domain.domain import Movie
from src.domain.domain import Client
from src.repository.client_repository import *
from src.repository.movie_repository import *
from src.services.client_service import *
import copy
from src.services.movie_service import *
class Test_clients(TestCase):
    def setUp(self) :
        self.client=Client(12,"Alex")
    def test_get_id(self):
        self.assertEqual(self.client.client_id,12)
    def test_get_name(self):
        self.assertEqual(self.client.name,"Alex")
    def test_set_id(self):
        self.client.client_id=2
        self.assertEqual(self.client.client_id,2)
    def test_set_name(self):
        self.client.name="Diana"
        self.assertEqual(self.client.name,"Diana")
    def test_str(self):
        self.assertEqual(str(self.client),"12,Alex")

class Test_movie(TestCase):
    def setUp(self) :
        self.movie=Movie(12,"Spiderman","a spider","SF")
    def test_get_id(self):
        self.assertEqual(self.movie.movie_id,12)
    def test_get_title(self):
        self.assertEqual(self.movie.title,"Spiderman")
    def test_get_description(self):
        self.assertEqual(self.movie.description,"a spider")
    def test_get_genre(self):
        self.assertEqual(self.movie.genre,"SF")
    def test_set_id(self):
        self.movie.movie_id=2
        self.assertEqual(self.movie.movie_id,2)
    def test_set_title(self):
        self.movie.title="Frozen"
        self.assertEqual(self.movie.title,"Frozen")
    def test_set_description(self):
        self.movie.description="about Elsa"
        self.assertEqual(self.movie.description,"about Elsa")
    def test_set_genre(self):
        self.movie.genre="family"
        self.assertEqual(self.movie.genre,"family")
    def test_str(self):
        self.assertEqual(str(self.movie),"12,Spiderman,a spider,SF")

class Test_client_repo(TestCase):
    def setUp(self) :
        self.repo=ClientRepo("test_client.txt")
        self.repo.change_data_client([])
        self.repo._save__file()
    def test_save(self):
        self.repo.ADD_client(Client(1222,"Elena"))
        self.repo._save__file()
        fin=open("test_client.txt","rt")
        self.assertEqual(fin.read(),"1222,Elena\n")
        fin.close()
    def test_add(self):
        one=Client(12,"Diana")
        self.repo.ADD_client(one)
        clients=self.repo.get_all_client()
        self.assertEqual(clients[0],one)
    def test_load(self):
        one=Client(1222, "Elena")
        self.repo.ADD_client(one)
        self.repo._save__file()
        try:
            self.repo._load_file()
        except:
            print("load didn't work")
        clients = self.repo.get_all_client()
        self.assertEqual(clients[0], one)

    def test_delet(self):
        self.repo.ADD_client(Client(1222, "Elena"))
        self.repo.delete_client(0)
        self.assertEqual(self.repo.get_all_client(),[])
    def test_change(self):
        self.repo.ADD_client(Client(1222, "Elena"))
        one=Client(111,"Diana")
        self.repo.change_client(0,one)
        clients = self.repo.get_all_client()
        self.assertEqual(clients[0],one)
    def test_get_all(self):
        one = Client(111, "Diana")
        self.repo.ADD_client(one)
        list=[one]
        self.assertEqual(list,self.repo.get_all_client())

class Test_Movie_repo(TestCase):
    def setUp(self) :
        self.repo=MovieRepo("test_movie.txt")
        self.repo.change_data_movie([])
        self.repo._save__file()
    def test_save(self):
        self.repo.ADD_movie(Movie(12,"Spiderman","a spider","SF"))
        self.repo._save__file()
        fin=open("test_movie.txt","rt")
        self.assertEqual(fin.read(),"12,Spiderman,a spider,SF\n")
        fin.close()
    def test_load(self):
        one=Movie(12,"Spiderman","a spider","SF")
        self.repo.ADD_movie(one)
        self.repo._save__file()
        try:
            self.repo._load_file()
        except:
            print("load didn't work")
        clients = self.repo.get_all_movie()
        self.assertEqual(clients[0], one)
    def test_ADD(self):
        one = Movie(12, "Spiderman", "a spider", "SF")
        self.repo.ADD_movie(one)
        clients = self.repo.get_all_movie()
        self.assertEqual(clients[0], one)
    def test_delet(self):
        self.repo.ADD_movie(Movie(12, "Spiderman", "a spider", "SF"))
        self.repo.delete_movie(0)
        self.assertEqual(self.repo.get_all_movie(),[])
    def test_get_all(self):
        one = Movie(12, "Spiderman", "a spider", "SF")
        self.repo.ADD_movie(one)
        list=[one]
        self.assertEqual(list,self.repo.get_all_movie())
    def test_change(self):
        self.repo.ADD_movie(Movie(13,"Frozen","about Elsa","family"))
        one = Movie(12, "Spiderman", "a spider", "SF")
        self.repo.change_movie(0,one)
        clients = self.repo.get_all_movie()
        self.assertEqual(clients[0],one)

class Test_client_service(TestCase):
    def setUp(self) :
        self.service=ClientService(ClientRepo("test_client.txt"))
    def test_add(self):
        clientul=Client(123,'Diana')
        self.service.add_client(clientul)
        list=self.service.return_all_client()
        self.assertEqual(list[len(list)-1],clientul)
    def test_remove(self):
        list=copy.deepcopy(self.service.return_all_client())
        self.service.add_client(Client(12000, "Elena"))
        self.service.remove_client(12000)
        self.assertEqual(self.service.return_all_client(),list)
    def test_update(self):
        self.service.add_client(Client(12000, "Elena"))
        self.service.update_client(12000,"Adina")
        list = copy.deepcopy(self.service.return_all_client())
        self.assertEqual(list[len(list)-1],Client(12000,"Adina"))
class Test_movie_service(TestCase):
    def setUp(self) :
        self.service=MovieService(MovieRepo("test_movie.txt"))
    def test_add(self):
        filmul=Movie(13,"Knifes out","a crime","crime")
        self.service.add_movie(filmul)
        list=self.service.return_all_movie()
        self.assertEqual(list[len(list)-1],filmul)
    def test_remove(self):
        list=self.service.return_all_movie()
        self.service.add_movie(Movie(120000,"Name","a dog",'sf'))
        self.service.remove_movie(120000)
        self.assertEqual(list,self.service.return_all_movie())
    def test_update(self):
        self.service.add_movie(Movie(120000, "Name", "a dog", 'sf'))
        self.service.update_movie(120000,"NoName","a boy without a name","mystery")
        list = self.service.return_all_movie()
        self.assertEqual(str(list[len(list)-1]),str(Movie(120000,"NoName","a boy without a name","mystery")))
if __name__ == '__main__':
    unittest.main()





