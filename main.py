from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
import requests
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

API_KEY = "Jeak1Ey102Ghf7pAm_Ot4j4Gv7cslXYH"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
HEADERS = {
    "apikey": API_KEY
}
param = {
    "fly_from": "LON",
    "date_from": "16/12/2022",
    "date_to": "16/06/2023"
}
search = FlightSearch()
# search.get_iata_code("London")
# sheety = DataManager()
# sheety.add_iata_code()
# sheety = FlightData()
# sheety.get_flight_information()
flight = NotificationManager()
flight.send_message()


# response = requests.get(url=FLIGHTSEARCH_ENDPOINT, headers=HEADERS, params=param)
# response.raise_for_status()
# result = response.json()
# print(result)