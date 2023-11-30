import smtplib
import datetime as dt
import random

MY_EMAIL = "senderemail@gmail.com"
APP_PASSWORD = "tiifojvwswtcoklyunasasd"


def send_email(subject, body):
    # print(subject)
    # print(body)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure our connection
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="receiveremail@yahoo.com",
            msg=f"Subject:{subject}\n\n{body}"
        )


if dt.datetime.now().weekday() == 0:
    with open("quotes.txt", "r") as f:
        quote_list = f.readlines()
        email_body = random.choice(quote_list)
        send_email(subject="Monday Motivation", body=email_body)

# now = dt.datetime.now().weekday()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
#
# print(type(day_of_week))
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1988, month=1, day=31)
