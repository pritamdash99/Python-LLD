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

class OrderService:
    def __init__(self, email_service: NotificationService):
        self.__email_service = email_service

    # .send() of our email service will be called to send email about product order.
    def create_order(self):
        self.__email_service.send("info@abc.com","New Order","Order has been Placed")

ens = EmailNotificationService()
orderService = OrderService(ens)
orderService.create_order()
"""
Sending Email through EmailNotificationService
To = info@abc.com
Title = New Order
Body = Order has been Placed
"""

"""
ISSUE - We can't use the same way to access SendGridEmailService

send_grid_service = SendGridEmailService()
orderService = OrderService(send_grid_service)

1. OrderService() accepts a NotificationService but SendGridEmailService is not a NotificationService
2. orderService.create_order() will throw error as SendGridEmailService doesn't have .send() method.

So, we need a way -
    to make 2 different components which aren't compatible with each other normally, become compatible.

Thus Adapter Pattern.
"""