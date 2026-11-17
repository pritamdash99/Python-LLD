# High Level Module 
from email_service import EmailService
from sms_service import SMSService

class NotificationService:
    def __init__(self) -> None:
        #We create objects of both low level modules inside high level constructors
        #This way the high level module is directly dependent on both low level modules.
        self.email_service = EmailService()
        self.sms_service = SMSService()

    def notifyByEmail(self,message):
        self.email_service.send_email(message)

    def notifyBySMS(self,message):
        self.sms_service.send_sms(message)

ns = NotificationService()
ns.notifyByEmail("Hope This Email Finds You Will")
ns.notifyBySMS("Sms right at you!")
# Sending Email : Hope This Email Finds You Will
# Sending SMS: Sms right at you!
"""
This tightly coupled high dependency of higher module on low module go against DIP.
+
There's no more flexibility! 
    If later we need to build another low level module "whatsapp service" 
    we'll need to make changes to - high level module "NotificationService"'s constructor. 
    That's bad practice.
+
No testing freedom - Making changes to high level constructor opens door to new bugs in already tested code.
"""
