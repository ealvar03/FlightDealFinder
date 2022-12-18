from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.


search = FlightSearch()
# search.get_iata_code("London")
# sheety = DataManager()
# sheety.add_iata_code()
# sheety = FlightData()
# sheety.get_flight_information()
flight = NotificationManager()
flight.send_message()

