from flight_search import FlightSearch
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/a0c55b0295b015ec40122f99a8becedd/flightDeals/prices"


class DataManager:

    def add_iata_code(self):
        """
        Gets the 'iata code' from the API corresponding with the selected city and adds it using Sheety API to the
        Google sheet
        :return: updated Google sheet
        """
        response = requests.get(url=SHEETY_ENDPOINT)
        result = response.json()
        flight_searcher = FlightSearch()
        for d in result['prices']:
            params = {
                "price": {
                    "iataCode": flight_searcher.get_iata_code_from_teq(d['city'])
                }
            }
            updated_response = requests.put(url=f"{SHEETY_ENDPOINT}/{d['id']}", json=params)
            updated_response.raise_for_status()
            return updated_response.json()
