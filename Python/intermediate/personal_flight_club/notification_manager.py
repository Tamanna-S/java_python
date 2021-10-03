from twilio.rest import Client
from smtplib import SMTP

TWILIO_SID = "AC8b6781c3fd6f2b73db04487df563204e"
TWILIO_AUTH_TOKEN = "ba477a109da9cda49d7327fec4fa9b15"
TWILIO_VIRTUAL_NUMBER = "+19893107947"
YOUR_NUMBER = "+919990794499"

EMAIL = "kanishka.sharma08102008@gmail.com"
PASSORD = "K.SH@RM@123"


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