import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.data = []

    def get_data(self):
        url = "https://api.sheety.co/b755188ae7d54bb8e8082a67e3f21400/flightDeals/prices"
        response = requests.get(url = url)
        print(response.json())
        self.data = response.json()["prices"]
        print(self.data)
        return self.data

    def update_data(self, data):
        url = f"https://api.sheety.co/b755188ae7d54bb8e8082a67e3f21400/flightDeals/prices/{data['id']}"
        new_data = {
            "price": {
                "iataCode" : data["iataCode"]
            }
        }

        response = requests.put(url = url, json=new_data)
        print(response.text)