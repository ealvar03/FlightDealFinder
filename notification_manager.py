from twilio.rest import Client


class NotificationManager:
    account_sid = "AC74ba290819e2a0f532ff2522c2b18e4b"
    auth_token = "93d26ad80b860971b7cfc5025f5f31a9"

    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self):
        client = Client(self.account_sid, self.auth_token)
        # message = client.messages \
        #     .create(
        #     body=f"Low price alert! Only {price}GBP to fly from {departure_city}-{departure_airport} "
        #          f"to {destination_city}-{destination_airport}, from {arrival_date} to {departure_date}",
        #     from_='+14095097627',
        #     to='+447899630943'
        # )
        print(f"Low price alert! Only {price}GBP to fly from {departure_city}-{departure_airport} "
              f"to {destination_city}-{destination_airport}, from {arrival_date} to {departure_date}")
