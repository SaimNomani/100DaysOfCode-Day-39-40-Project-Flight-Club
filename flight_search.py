import requests
from pprint import pprint
from flight_data import FlightData
from datetime import datetime, timedelta
from data import TEQUILA_API_ENDPOINT, TEQUILA_API_KEY
# current_date=datetime().now().date().strftime("%d/%m/%Y")
# current_time=datetime().now().time().strftime("%H/%M/%S")
# date_after_6_monthes=current_date+timedelta(days=6*30)


class FlightSearch:
 #This class is responsible for talking to the Flight Search API.
    def get_iata(self, city):
        params={
            "term":city,
            "location_types": "city",
        }
        headers={
            "apikey": TEQUILA_API_KEY,
        }
        tequila_response=requests.get(url=f"{TEQUILA_API_ENDPOINT}/locations/query", params=params, headers=headers)
        tequila_response.raise_for_status()
        # print(tequila_response.status_code)
        # print(tequila_response.json())
        iata=tequila_response.json()['locations'][0]['code']
        return iata
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_API_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
        try:
                data=response.json()['data'][0]
                print("\n\n")
                pprint(response.json())
                print("\n\n")


        except:

            print(f"No flights found for {destination_city_code}")
            return None
        else:
            flight_data=FlightData(price=data['price'],
                                    departure_city=data['route'][0]['cityCodeFrom'],
                                    arrival_city=data['route'][0]['cityCodeTo'],
                                    departure_airport_code=data['route'][0]['flyFrom'],
                                    arrival_airport_code=data['route'][0]['flyTo'],
                                    departure_date=data['route'][0]['local_departure'].split('T')[0],
                                    return_date=data['route'][1]['local_departure'].split('T')[0],
                                    )
            print(f"{flight_data.arrival_city}: £{flight_data.price}")
            return flight_data
