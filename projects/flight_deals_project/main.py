from projects.flight_deals_project.data_manager import DataManager
from projects.flight_deals_project.flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_data()
# pprint(sheet_data)

for data in sheet_data:
    if len(data["iataCode"]) != 0:
        flight_search = FlightSearch()
        data["iataCode"] = flight_search.get_destination_code(data)
        data_manager.update_data(data)


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.