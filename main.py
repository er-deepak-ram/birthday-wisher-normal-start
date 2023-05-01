import datetime as dt
import pandas
import random
import smtplib


PLACE_HOLDER = "[NAME]"

sender_email = "deepak.kumar2305@gmail.com"
password = "zgvkrwjgikynbwyw"
receiver = "nightrider.180@gmail.com"
cc = "er.deepak.kumar2305@gmail.com"
message_subject = "Subject:Happy Birthday!"

today_date = dt.datetime.today()
today = (today_date.month, today_date.day)

birthday_file = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in birthday_file.iterrows()}

if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        message = "From: %s\r\n" % sender_email + "To: %s\r\n" % birthday_person["email"] + "CC: %s\r\n" % cc + "Subject: %s\r\n" % message_subject + "\r\n" + contents
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=birthday_person["email"], msg=message)



