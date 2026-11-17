#This the class we use for testing and running the logics.

from notification_service import NotificationService
from sms_service import SmsService
from email_service import EmailService

sms_service = SmsService()
email_service = EmailService()

sms_notification = NotificationService(sms_service)
email_notification = NotificationService(email_service)

sms_notification.notify("Did you reach?")
email_notification.notify("Congratulations!!!")

# Sending SMS : Did you reach?
# Sending Email : Congratulations!!!

"""
This de-coupled way of writing supports DIP
If we need to add another notification service - 
    We won't need to make changes in the High Level Modules [Channel + Service]
    Just create a new file -> 
    implement the logic -> 
    import class in main.py ->
    Create object in main.py -> 
    run the function
"""
