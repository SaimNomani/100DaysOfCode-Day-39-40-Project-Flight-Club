#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from customers import Customer

data_manager=DataManager()
flight_search=FlightSearch()
notification_manager=NotificationManager()
customer=Customer()

sheet_data=data_manager.get_flight_data()
if sheet_data[0]['iataCode'] =='':
    for row in sheet_data:
        iata=flight_search.get_iata(row['city'])
        row['iataCode']=iata
    print(sheet_data)
    data_manager.destination_data=sheet_data
    data_manager.update_iata()

ORIGIN_CITY_IATA='LON'
tomorrow=datetime.now()+timedelta(days=1)
date_after_6_monthes=datetime.now()+timedelta(days=6*30)
for destination in sheet_data:
    flight=flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        tomorrow,
        date_after_6_monthes
     )
    if flight is None:
        continue
    if flight.price<=destination['lowestPrice']:
        message=f"Low price alert! only £{flight.price} to fly from {flight.departure_city}-{flight.departure_airport_code} to {flight.arrival_city}-{flight.arrival_airport_code}, from {flight.departure_date} to {flight.return_date}"

        customer.get_message(message)
