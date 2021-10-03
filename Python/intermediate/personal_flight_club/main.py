#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta

from flight_search import FlightSearch
flight_search = FlightSearch()

from data_manager import DataManager
data_manager = DataManager()

from users import Users
start = Users()

from notification_manager import NotificationManager
notification_manager = NotificationManager()

start.firststep()

ORIGIN_CITY_IATA = "IND"
sheet_data = data_manager.get_destination_data()

for data in sheet_data:
    
    if data["iataCode"] == "-":
    
            data["iataCode"] = flight_search.get_destination_code(data["city"])

            data_manager.destination_data = sheet_data
            data_manager.update_destination_code()
    

tomorrow = datetime.now() + timedelta(days= 1 )
six_month_from_today = datetime.now() + timedelta(days= (6*30))


for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight == None:
        pass

    elif destination["lowestPrice"] == "-":
        destination["lowestPrice"] = flight.price
        data_manager.update_price(flight.price, destination["id"])
        sheet_data = data_manager.get_destination_data()
        

    elif flight.price < destination["lowestPrice"]:

            users = start.get_user_data()
            emails = [row["email"] for row in users]
            names = [row["firstName"]+row["lastName"] for row in users]


            msg=f"Low price alert! Only Rs.{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

            if flight.stop_overs > 0:
                msg += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            
            notification_manager.send_msg(msg)
            notification_manager.send_email(msg, emails)
            print(f"please check your email.")

            data_manager.update_price(flight.price, destination["id"])
            sheet_data = data_manager.get_destination_data()

