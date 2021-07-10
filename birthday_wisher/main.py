import datetime as dt
import random
import pandas
import smtplib

def mail_birthday_wishes(message, target_email):
    my_email = "testingmain19@gmail.com"
    passwor = "Qwerty@12345"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=passwor)
    connection.sendmail(from_addr=my_email, to_addrs=target_email,
                        msg=f"Subject: Birthday wishes\n\n {message}")
    connection.close()




today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthday_date = {(data_row.month, data_row.day) : data_row for (index, data_row) in data.iterrows() }
print(birthday_date)


if today in birthday_date:
    birthday_person = birthday_date[today]
    file_name = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_name) as file:
        content =  file.read()
        contents = content.replace("[NAME]", birthday_person["name"])
        mail_birthday_wishes(contents, birthday_person.email)
