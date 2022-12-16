import requests
from flight_data import FlightData
from datetime import datetime, timedelta

HEADERS = {
            "apikey": "Jeak1Ey102Ghf7pAm_Ot4j4Gv7cslXYH"
        }
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"


class FlightSearch:

    def get_iata_code_from_teq(self, city):
        params = {
            "term": city
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=HEADERS, params=params)
        code = response.json()['locations'][0]['code']
        return code

    def get_flight_information(self):
        self.response = requests.get(url=SHEETY_ENDPOINT)
        self.result = self.response.json()
        for d in self.result['prices']:
            city_iata = d['iataCode']
            tomorrow = datetime.now() + timedelta(days=1)
            six_months = datetime.now() + timedelta(days=(6 * 30))
            params = {
                "fly_from": "LON",
                "fly_to": city_iata,
                "date_from": tomorrow.strftime("%d/%m/%Y"),
                "date_to": six_months.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
            }
            tequila_response = requests.get(url=TEQUILA_ENDPOINT, params=params, headers=HEADERS)
            try:
                data = tequila_response.json()['data'][0]
            except IndexError:
                print(f"No flights found for {city_iata}.")
                return None

            flight_data = FlightData(
                price=data['price'], departure_city=data['route'][0]['cityFrom'],
                departure_airport=data['route'][0]['flyFrom'],destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                arrival_date=data['route'][0]['local_departure'].split("T")[0],
                departure_date=data['route'][1]['local_departure'].split("T")[0])
            return flight_data
