from twilio.rest import Client

class NotificationManager:
    account_sid = "Account_sid"
    auth_token = "Auth_token"

    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self):
        client = Client(self.account_sid, self.auth_token)
        # message = client.messages \
        #     .create(
        #     body=f"Low price alert! Only {price}GBP to fly from {departure_city}-{departure_airport} "
        #          f"to {destination_city}-{destination_airport}, from {arrival_date} to {departure_date}",
        #     from_='+14095097627',
        #     to='+44'
        # )
        # print(f"Low price alert! Only {price}GBP to fly from {departure_city}-{departure_airport} "
        #       f"to {destination_city}-{destination_airport}, from {arrival_date} to {departure_date}")
