from twilio.rest import Client
from smtplib import SMTP

TWILIO_SID = "YOUR_SID"
TWILIO_AUTH_TOKEN = "YOUR_AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER = "VIRTUAL_NUMBER"
YOUR_NUMBER = "YOUR_NUMBER"

EMAIL = "YOUR_EMAIL"
PASSORD = "YOUR_PASSWORD"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_msg(self, msg) :
        message = self.client.messages.create(
            body = msg,
            from_ = TWILIO_VIRTUAL_NUMBER,
            to= YOUR_NUMBER
        )

    def send_email(self, msg, emails) :
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSORD)
            for email in emails:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=email,
                    msg= f"Subject:New Low Price Flight!\n\n{msg}"
                )
