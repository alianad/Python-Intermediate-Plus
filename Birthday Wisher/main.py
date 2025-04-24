from datetime import datetime
from dotenv import load_dotenv
import os
import pandas
import random
import smtplib

load_dotenv()

EMAIL = "alia.nadhira29@gmail.com"
PASSWORD = os.getenv("password")
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdate_dictionary = {(row["month"], row["day"]) : row for (index, row) in data.iterrows()}

if today_tuple in birthdate_dictionary:

    birthdate_person = birthdate_dictionary[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_contents = contents.replace("[NAME]", birthdate_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs= birthdate_person["email"],
            msg=f"Subject :Happy Birthday !\n\n{new_contents}"
        )
