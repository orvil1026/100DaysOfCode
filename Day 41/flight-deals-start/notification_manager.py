from twilio.rest import Client
from decouple import config
import smtplib


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure


class NotificationManager:

    # This class is responsible for sending notifications with the deal flight details.

    def send_message(self, flight_data):
        account_sid = config('TWILIO_SID')
        auth_token = config('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"Low price alert!! Only ₹{flight_data.price} to fly from {flight_data.dep_city}-{flight_data.dept_iata}"
            f"to {flight_data.arr_city}-{flight_data.arr_iata} ,from {flight_data.outbound_dt} to {flight_data.inbound_dt}",
            from_=config('PHONE_NO_FROM'),
            to=config('PHONE_NO_TO')
        )
        print(message.sid)

    def send_mail(self, email, flight_data):
        my_email = config("EMAIL")
        password = config("PASSWORD")

        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()

        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Flight Deal!Low price alert!!\n Only {flight_data.price} to fly from {flight_data.dep_city}-{flight_data.dept_iata}"
            f"to {flight_data.arr_city}-{flight_data.arr_iata} ,from {flight_data.outbound_dt} to {flight_data.inbound_dt}"
        )

        connection.close()

