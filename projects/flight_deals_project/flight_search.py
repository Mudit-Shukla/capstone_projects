import requests
class FlightSearch:

    TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
    TEQUILA_API_KEY = "qFn_wZooZaSSbdzQ5fJHrjNFl-WifoDd"
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, data):
        global TEQUILA_API_KEY, TEQUILA_ENDPOINT
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": data, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results["code"]
        return code
