from twilio.rest import Client

ACCOUNT_SID = "Account Sid"
AUTH_TOKEN = "Auth token"


class NotificationManager:

    def send_message(self, message):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        sms = client.messages.create(
            body=message,
            from_='+14095097627',
            to='Your phone number'
        )

