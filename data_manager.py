from flight_search import FlightSearch
import requests

SHEETY_PRICES_ENDPOINT = "Sheety prices endpoint"
SHHETY_USERS_ENDPOINT = "Sheety users endpoint"


class DataManager:

    def __init__(self):
        self.dest_data = {}

    def get_destination_data(self):
        """
        It retrieves the information from the Google sheet using the Sheety API call.
        """

        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        result = response.json()
        self.dest_data = result['prices']
        return self.dest_data

    def add_iata_code(self):
        """
        Gets the 'iata code' from the API corresponding with the selected city and adds it using Sheety API to the
        Google sheet
        :return: updated Google sheet
        """

        flight_searcher = FlightSearch()
        for d in self.dest_data:
            params = {
                "price": {
                    "iataCode": flight_searcher.get_iata_code_from_teq(d['city'])
                }
            }
            updated_response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{d['id']}", json=params)
            updated_response.raise_for_status()
            return updated_response.json()

    def add_destination(self, city, iata_code, price):
        """
        It adds a new row into the Google sheet using Sheety API.
        """

        parameters = {
            "price": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": price
            }
        }

        response = requests.post(url=SHEETY_PRICES_ENDPOINT, json=parameters)
        return response.json()

    def get_user_mails(self):
        """
        It iterates through the Google users sheet and retrieves the users mail using Sheety API
        """

        response = requests.get(url=SHHETY_USERS_ENDPOINT)
        data = response.json()
        return data['users']
