from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


search = FlightSearch()
sheet_data = DataManager()
text_message = NotificationManager()

for d in sheet_data.get_destination_data():
    flight = search.get_flight_information(d['iataCode'])
    if flight.price < d['lowestPrice']:
        text_message.send_message(message=f"Low price alert! Only {flight.price}GBP to fly from "
                                          f"{flight.departure_city}-{flight.departure_airport} "
                                          f"to {flight.destination_city}-{flight.destination_airport}, "
                                          f"from {flight.arrival_date} to {flight.departure_date}")


