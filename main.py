##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random
import smtplib
import os

APP_PASSWORD = os.environ.get("APP_PASSWORD")
MY_EMAIL = os.environ.get("MY_EMAIL")

data = pandas.read_csv("./birthdays.csv")
month = dt.datetime.now().month
day = dt.datetime.now().day
for index, row in data.iterrows():
    if row.month == month and row.day == day:
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            letter = file.read()
        new_letter = letter.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(to_addrs=row.email, from_addr=MY_EMAIL, msg=f"Subject:Happy Birthday {row["name"]}\n\n{new_letter}")
        


