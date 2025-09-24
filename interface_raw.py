from abc import ABC, abstractmethod

class NofiticationSender(ABC):

    @abstractmethod
    def send_notification(self, message : str) -> None:
        pass


class EmailNotificationSender():

    def send_notification(self, message : str) -> None:
        print(message)

obj = EmailNotificationSender()
obj.send_notification('Hello World')