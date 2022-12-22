import requests
from flight_data import FlightData
from datetime import datetime, timedelta
from pprint import pprint

HEADERS = {
    "apikey": "API Key"
}
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"


class FlightSearch:

    def get_iata_code_from_teq(self, city):
        """
         It gets the iata code from the Tequila flight API that corresponds to the selected city when is called.
        :return: iata code
        """

        params = {
            "term": city
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=HEADERS, params=params)
        code = response.json()['locations'][0]['code']
        return code

    def get_flight_information(self, destination_iata_city):
        """
        This function will retrieve the information from the Tequila API under the parameters that have been defined
        :param destination_iata_city: The corresponding city from the Google sheet.
        :return: the data from the Tequila API that corresponds with all the requirements predefined as parameters
        """

        tomorrow = datetime.now() + timedelta(days=1)
        six_months = datetime.now() + timedelta(days=(6 * 30))
        params = {
            "fly_from": "LON",
            "fly_to": destination_iata_city,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        tequila_response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers=HEADERS)
        try:
            data = tequila_response.json()['data'][0]
        except IndexError:
            params['max_stopovers'] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers=HEADERS)
            try:
                data = response.json()['data'][0]
                pprint(data)
            except IndexError:
                return None
            else:
                flight_data = FlightData(
                    price=data['price'],
                    departure_city=data['route'][0]['cityFrom'],
                    departure_airport=data['route'][0]['flyFrom'],
                    destination_city=data['route'][0]['cityTo'],
                    destination_airport=data['route'][0]['flyTo'],
                    arrival_date=data['route'][0]['local_departure'].split("T")[0],
                    departure_date=data['route'][1]['local_departure'].split("T")[0],
                    stop_overs=1,
                    via_city=data['route'][0]['cityTo'])
                return flight_data
        else:
            flight_data = FlightData(
                price=data['price'],
                departure_city=data['route'][0]['cityFrom'],
                departure_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                arrival_date=data['route'][0]['local_departure'].split("T")[0],
                departure_date=data['route'][1]['local_departure'].split("T")[0])
            return flight_data
