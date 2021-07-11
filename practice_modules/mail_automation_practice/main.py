import smtplib
import datetime as dt
import random

def mail_to_client(message):
    my_email = "testingmain19@gmail.com"
    passwor = "Qwerty@12345"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user = my_email , password = passwor)
    connection.sendmail(from_addr= my_email, to_addrs= "muditshukla010@gmail.com", msg=f"Subject: Tuesday Motivation\n\n {message}")
    connection.close()

with open ("quotes.txt") as file:
    quotes_list = (file.readlines())

today_date = dt.datetime.now()
if today_date.isoweekday():
    mail_to_client(random.choice(quotes_list))