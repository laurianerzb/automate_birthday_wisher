import pandas as pd
import random
import smtplib
import datetime as dt

MY_EMAIL = "your@email.com"
PASSWORD = ""

current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day
month_day = (current_month, current_day)
birthdays = pd.read_csv('./data/birthdays_file/birthdays.csv')


birthdays_dict = {
    (data_row['month'], data_row['day']): data_row for (index, data_row) in birthdays.iterrows()
}

file_path = f'./data/letter_templates/letter{random.randint(1, 3)}'
if month_day in birthdays_dict:
    birthday_person = birthdays_dict[month_day]
    with open(file_path, 'r') as letter:
        message = letter.read()
        message = message.replace('[NAME]', birthday_person['name'])
        print(message)
    with smtplib.SMTP('smtp.gmail.com', 465) as connection:
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person['email'],
            msg=f'Happy Birthday\n\n{message}'
        )
