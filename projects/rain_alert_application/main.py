import requests
import smtplib

LATITUDE = -33.924870
LONGITUDE = 18.424055

MY_EMAIL = "testingmain19@gmail.com"
TARGET_ADDRESS = "muditshukla010@gmail.com"
PASSWORD = "Qwerty@12345"

def mail_warning():
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(MY_EMAIL,PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs = TARGET_ADDRESS,
                        msg = "Subject: Rain Alert"
                              "\n\n There is a probability of rain today\n\n "
                              "Do not forget to take you umbrella \n\n"
                              " Have a cheerful day"
                        )


parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": "cea842251268b3ed11db5770a43f1743",
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
useful_data = (response.json()["hourly"])

for i in range(6,19):
    data = useful_data[i]["weather"][0]["id"]
    if data < 700:
        mail_warning()
        break
