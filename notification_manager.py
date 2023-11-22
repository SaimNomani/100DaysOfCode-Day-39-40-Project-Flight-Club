from smtplib import SMTP
from data import RECIEVERS_EMAIL, MY_EMAIL, MY_PASSWORD
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass
    def send_mail(self, message, customer_email):
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                 to_addrs=customer_email,
                                   msg=f"subject:flight alert\n\n{message}".encode('utf-8')
                                   )
            print("sent")