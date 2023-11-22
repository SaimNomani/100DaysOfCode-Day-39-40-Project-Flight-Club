from pprint import pprint
import requests
from data import SHEETY_ENDPOINT

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.destination_data={}
    def get_flight_data(self):
        sheety_response=requests.get(url=SHEETY_ENDPOINT)
        self.destination_data=sheety_response.json()['prices']
        return self.destination_data
    def update_iata(self):
        for city in self.destination_data:
            params={
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            post_response=requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=params)
            print(post_response.text)
