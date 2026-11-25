from abc import ABC, abstractmethod

#Interface
class NotificationService(ABC):
    @abstractmethod
    def send(self, to: str, title: str, body: str): pass

#Type 1 of Email Service
class EmailNotificationService(NotificationService):

    def send(self, to: str, title: str, body: str):
        print("\nSending Email through EmailNotificationService")
        print(f"To = {to}")
        print(f"Title = {title}")
        print(f"Body = {body}")

#Another type of Email Service
class SendGridEmailService:

    def send_email(self,recipient : str, subject : str, content : str):
        print("\nSending Email through SendGridEmailService")
        print(f"Recipient = {recipient}")
        print(f"Subject = {subject}")
        print(f"Content = {content}")

# We thus create an Adapter for SendGrid to make it a Notification Type & be able to call .send()

class SendGridAdapter(NotificationService):
    def __init__(self, sendGridService: SendGridEmailService) -> None:
        self.__sendGridService = sendGridService

    def send(self, to: str, title: str, body: str):
        #We pass the arguments and make this .send() act as .send_email()
        self.__sendGridService.send_email(to,title,body)

# Client code - need not be updated anymore when a new email sender type gets added.
class OrderService:
    def __init__(self, email_service: NotificationService):
        self.__email_service = email_service

    # .send() of our email service will be called to send email about product order.
    def create_order(self):
        self.__email_service.send("info@abc.com","New Order","Order has been Placed")

    def updateServiceType(self, emailService : NotificationService):
        self.__email_service = emailService

ens = EmailNotificationService()
orderService = OrderService(ens)
orderService.create_order()

print("==============")

send_grid_service = SendGridEmailService()
send_grid_adapter = SendGridAdapter(send_grid_service)
orderService.updateServiceType(send_grid_adapter)
orderService.create_order()

"""
Sending Email through EmailNotificationService
To = info@abc.com
Title = New Order
Body = Order has been Placed
==============

Sending Email through SendGridEmailService
Recipient = info@abc.com
Subject = New Order
Content = Order has been Placed
"""



