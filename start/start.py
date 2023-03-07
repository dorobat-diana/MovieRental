from src.ui.ui import *
from src.repository.movie_repository import *
from src.repository.client_repository import *
from src.repository.rental_repository import *
from src.services.client_service import *
from src.services.rental_service import *
from src.services.movie_service import *


if __name__ == "__main__":
    rep_movie= MovieRepo("movie.txt")
    rep_client= ClientRepo("client.txt")
    rep_rental= RentalRepo("rental.txt")
    ser_movie= MovieService(rep_movie)
    ser_client= ClientService(rep_client)
    ser_rental= RentalService(rep_rental)
    UI=UserInterface(ser_movie, ser_client, ser_rental)
    UI.menu()