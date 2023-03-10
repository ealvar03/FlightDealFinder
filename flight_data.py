class FlightData:

    def __init__(self, price, departure_city, departure_airport, destination_city, destination_airport,
                 arrival_date, departure_date, stop_overs= 0, via_city=""):
        """
        It is responsible for storing and structuring the flight data model.
        """

        self.price = price
        self.departure_city = departure_city
        self.departure_airport = departure_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.stop_overs = stop_overs
        self.via_city = via_city


