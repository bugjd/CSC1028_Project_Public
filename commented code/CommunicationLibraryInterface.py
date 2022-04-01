from unicodedata import decimal


class CommunicationLibraryInterface:
    """A blueprint on how this human program should communicate with the team members."""
    def __init__(self, sent_from: str, password: str, url: str):
        """The method creating a new Communication Object"""
        pass

    def send_email(self, email_address: str, person_name: str, task_name: str, uuid: str):
        """This method allows the project to send emails to team members regarding a certain task"""
        pass

    def send_email(self, email_address: str, person_name: str, description: str, content: str, uuid: str):
        """This method allows the project to send emails regarding anything"""
        pass

    def send_text(self, phone_number: int, countrycode: int, message: str) -> decimal:
        """This method allows messages to be sent and provides a decimal of how much it cost to send the message. if
        unable to send message a result of -1 in decminal form should be returned """

        def check_message_length() -> bool:
            """A method to check the message is not longer than 160 characters which is the SMS standard MAX size.
            also checks over zero """
            if len(message) <= 0 or message > 160:
                return False
            else:
                return True

        pass

    def send_push_notification(self, push_notification_id : int, message :str) -> bool:
        """A method to allow the communication to send push notfications to ones device. returns true if able to send
        notification"""
        pass



