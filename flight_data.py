from pprint import pprint
import requests
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_airport_code, departure_city, arrival_city, arrival_airport_code,departure_date,return_date, stop_overs=0, via_city=None):
        self.price=price
        self.departure_city=departure_city
        self.departure_airport_code=departure_airport_code
        self.arrival_city=arrival_city
        self.arrival_airport_code=arrival_airport_code
        self.departure_date=departure_date
        self.return_date=return_date
        self.stop_overs=stop_overs
        self.via_city=via_city
        

