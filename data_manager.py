from flight_search import FlightSearch
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/a0c55b0295b015ec40122f99a8becedd/flightDeals/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def add_iata_code(self):
        self.response = requests.get(url=SHEETY_ENDPOINT)
        self.result = self.response.json()
        self.flight_searcher = FlightSearch()
        for d in self.result['prices']:
            params = {
                "price": {
                    "iataCode": self.flight_searcher.get_iata_code_from_teq(d['city'])
                }
            }
            updated_response = requests.put(url=f"{SHEETY_ENDPOINT}/{d['id']}", json=params)
            updated_response.raise_for_status()
            return updated_response.json()
