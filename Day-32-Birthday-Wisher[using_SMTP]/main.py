##################### Extra Hard Starting Project ######################

import datetime as dt
import pandas
import os
import random
import smtplib

MY_EMAIL = "senderemail@gmail.com"
APP_PASSWORD = "tiiojvasdwwtcvbcoytklyun"

now = dt.datetime.now()
data_df = pandas.read_csv("birthdays.csv")


def get_email_text(name):
    letter = random.choice(letters)
    with open(f"letter_templates/{letter}", "r") as f:
        letter_text = f.read().replace("[NAME]", name)
    return letter_text


def send_email(email_to, body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure our connection
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email_to,
            msg=f"Subject:Happy Birthday!!!\n\n{body}"
        )


filtered_data = data_df.loc[(data_df['month'] == now.month) & (data_df['day'] == now.day)]
birthday_list = filtered_data.to_dict(orient="records")
if len(birthday_list) > 0:
    letters = os.listdir("letter_templates")
    for birthday in birthday_list:
        email_text = get_email_text(name=birthday['name'])
        send_email(email_to=birthday['email'], body=email_text)

# 1. Update the birthdays.csv - DONE

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
# actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
