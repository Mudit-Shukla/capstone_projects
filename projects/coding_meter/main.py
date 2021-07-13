import requests
import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN_ID = "Qwerty12345"
USERNAME = "daydreamer"

USER_PARAMS = {
    "token" : TOKEN_ID,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response.text)

GRAPH_ENDPOINT = PIXELA_ENDPOINT + "/" + USERNAME + "/graphs"

GRAPH_ID = "codegraph"
GRAPH_NAME = "code & code"
GRAPH_ENDPOINT_PARAMS = {
    "id" : GRAPH_ID,
    "name" : GRAPH_NAME,
    "unit" : "hour",
    "type" : "float",
    "color" : "ajisai"
}

GRAPH_HEADER = {
    "X-USER-TOKEN" : TOKEN_ID
}

# response = requests.post(url = GRAPH_ENDPOINT, json = GRAPH_ENDPOINT_PARAMS, headers=GRAPH_HEADER)
# print(response.text)

POST_ENDPOINT = GRAPH_ENDPOINT + "/" + GRAPH_ID

def get_date():
    date = ""
    return date.join((str(dt.datetime.now()).split(" ")[0].split("-")))

POST_ENDPOINT_PARAMS = {
    "date" : get_date(),
    "quantity" : "12.0",
}

response = requests.post(url = POST_ENDPOINT, json =POST_ENDPOINT_PARAMS, headers=GRAPH_HEADER)
print(response.text)

PUT_ENDPOINT = POST_ENDPOINT + "/" + get_date()

PUT_ENDPOINT_PARAMS = {
    "quantity" : "6.0"
}

# response = requests.put(url = PUT_ENDPOINT, json= PUT_ENDPOINT_PARAMS, headers = GRAPH_HEADER )
# print(response.text)

DELETE_ENDPOINT = PUT_ENDPOINT

# response = requests.delete(url = DELETE_ENDPOINT, json = PUT_ENDPOINT_PARAMS, headers = GRAPH_HEADER)