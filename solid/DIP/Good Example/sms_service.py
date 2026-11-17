#This low level module inherits the Mid-Interface
from notification_channel import NotificationChannel

class SmsService(NotificationChannel):
    def send(self, message: str):
        print(f"Sending SMS : {message}")
