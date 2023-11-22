from data import CUSTOMER_SHEET_ENDPOINT, BEARER_TOKEN
import requests
from notification_manager import NotificationManager
class Customer:
    def __init__(self) -> None:
        self.first_name=input("what is your first name: ")
        self.last_name=input("what is your last name: ")
        self.email1=input("enter your email: ")
        self.email2=input("enter your email again: ")
        while self.email1 != self.email2:
            self.email2=input("Wrong email. Enter your email again: ")
            if self.email1.lower()=='exit' or self.email1.lower()=='exit' or self.email1.lower()=='quiet' or self.email1.lower()=='quiet':
                exit()
        self.email=self.email1
        print("Welcome to Flight Club!!\n")
        self.post_customer_data()
        self.notification_manager=NotificationManager()
    def post_customer_data(self):
        params={
            "customer":{
                "firstName":self.first_name,
                "lastName":self.last_name,
                "email": self.email
            }
            
        }
        bearer_header={
                "Authorization": f"Bearer {BEARER_TOKEN}",
                "Content-Type":"application/json"
            }
        response=requests.post(url=CUSTOMER_SHEET_ENDPOINT, json=params, headers=bearer_header)
    def get_message(self, message):
        self.notification_manager.send_mail(message, self.email)
