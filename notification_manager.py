from twilio.rest import Client
import smtplib

ACCOUNT_SID = "Acc SID"
AUTH_TOKEN = "Auth Token"


class NotificationManager:

    def send_message(self, message):
        """
        It will generate a text message that will be sent to the number added on "to" with a flight notification.
        :param message: The body message corresponding to the flight deal
        """

        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        sms = client.messages.create(
            body=message,
            from_='Phone number',
            to='Phone number'
        )

    def send_emails(self, email, message):
        """
        It will send a email notification when it will be called.
        :param message: The body message corresponding to the flight deal
        """

        my_mail = "MY MAIL"
        password = "PASSWORD"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail, to_addrs=email, msg=f"Subject: New Low Price Flight!\n"
                                                                       f"{message}")

