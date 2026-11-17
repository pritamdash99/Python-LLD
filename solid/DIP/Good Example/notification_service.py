#This is the High-Level Module that only interacts with the Mid-Interface.

from notification_channel import NotificationChannel

class NotificationService:
    def __init__(self, channel : NotificationChannel) -> None:
        self.channel = channel
        #Inside this constructor we pass the respective channel to be used.

    def notify(self,message:str):
        self.channel.send(message)

