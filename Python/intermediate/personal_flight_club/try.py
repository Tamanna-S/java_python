import requests
from pprint import pp, pprint

TEQUILA_APIKEY = "4SkYnFiJX_a_ZP8NRs2HIWlyxqYRmjPK"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
header = {"apikey" : TEQUILA_APIKEY}
query = {
            "fly_from " : "IND",
            "fly_to" : "DPS",
            "date_from " : "03/09/2021",
            "date_to " : "01/01/2022",
            "nights_in_dst_from" : 7,
            "nights_in_dst_to" : 28,
            "flight_type" : "round",
            "one_for_city" : 1,
            "max_stopovers" : 1,
            "curr" : "INR"
        }

response = requests.get(search_endpoint, headers= header, params= query)
data = response.json()["data"][0]
pprint(data)

