import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:  # day is wednesday
    with open("quotes.txt") as file:
        quotes_list = file.readlines()
        random_quote = random.choice(quotes_list)

    my_email = '#'  # Your address
    password = '#'            # Your Password

    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(
        from_addr=my_email,
        to_addrs='#',  # receiver's address
        msg=f'Subject:Motivation\n\n{random_quote}'

    )
    connection.close()


