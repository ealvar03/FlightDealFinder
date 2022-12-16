import requests
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

HEADERS = {
    "apikey": "Jeak1Ey102Ghf7pAm_Ot4j4Gv7cslXYH"
}
SHEETY_ENDPOINT = "https://api.sheety.co/a0c55b0295b015ec40122f99a8becedd/flightDeals/prices"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_city, departure_airport, destination_city, destination_airport,
                 arrival_date, departure_date):
        self.price = price
        self.departure_city = departure_city
        self.departure_airport = departure_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.arrival_date = arrival_date
        self.departure_date = departure_date



