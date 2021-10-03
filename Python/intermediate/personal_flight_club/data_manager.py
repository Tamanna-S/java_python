import requests
from requests.models import Response

SHEET_ENDPOINT = "https://api.sheety.co/340901e51ddc58930c91a4d2b7f54662/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) :
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_code(self):

        for city in self.destination_data:
            new_data = {
                "price" :{
                    "iataCode" : city["iataCode"]
                }
            }
            response = requests.put(f"{SHEET_ENDPOINT}/{city['id']}", json= new_data)
    def update_price(self, new_price, id):
        new_data = {
            "price" :{
                "lowestPrice" : new_price
            }
        }
        response = requests.put(f"{SHEET_ENDPOINT}/{id}", json= new_data)
       

