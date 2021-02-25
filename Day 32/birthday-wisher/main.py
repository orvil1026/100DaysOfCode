
import pandas
import datetime as dt
import smtplib
import random

data = pandas.read_csv('birthdays.csv')  # Reading Csv data - birthdays

now = dt.datetime.now()
day = now.day
month = now.month

data_dict = data.to_dict(orient='records')
print(data_dict)

for row in data_dict:
    if row['month'] == month and row['day'] == day:
        name = row['name']
        email = row['email']
        letter_no = random.randint(1, 3)
        with open(f'./letter_templates/letter_{letter_no}.txt', mode='r') as letter:
            full_letter = letter.read()
            print(full_letter)
            new_letter = full_letter.replace('[NAME]', name)
            print(new_letter)

        my_email = '#'  # Your email address
        password = '#'  # Your Password

        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f'Subject:Happy Birthday!\n\n{new_letter}'
        )

        connection.close()





