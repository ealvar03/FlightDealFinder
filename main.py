from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
text_message = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    cities = [row["city"] for row in sheet_data]
    codes = search.get_iata_code_from_teq(cities)
    data_manager.add_iata_code()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}

for dest_code in destinations:
    flight = search.get_flight_information(dest_code)
    if flight is None:
        continue
    if flight.price < destinations[dest_code]['price']:
        users = data_manager.get_user_mails()
        emails = [row['email'] for row in users]
        names = [row['firstName'] for row in users]
        message = f"Low price alert! Only {flight.price}GBP to fly from {flight.departure_city}-" \
                  f"{flight.departure_airport} to {flight.destination_city}-{flight.destination_airport}," \
                  f"from {flight.arrival_date} to {flight.departure_date}.\n" \
                  f"https://www.google.co.uk/flights?hl=en#flt={flight.departure_airport}." \
                  f"{flight.destination_airport}.{flight.arrival_date}*{flight.destination_airport}." \
                  f"{flight.departure_airport}.{flight.departure_date}"
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        text_message.send_emails(emails, message)

###############################
# For the text message version:
###############################

# for d in sheet_data:
#     flight = search.get_flight_information(d['iataCode'])
#     if flight.price < d['lowestPrice']:
#         text_message.send_message(message=f"Low price alert! Only {flight.price}GBP to fly from "
#                                           f"{flight.departure_city}-{flight.departure_airport} "
#                                           f"to {flight.destination_city}-{flight.destination_airport}, "
#                                           f"from {flight.arrival_date} to {flight.departure_date}")



