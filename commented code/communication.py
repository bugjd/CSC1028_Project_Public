import smtplib
from CommunicationLibraryInterface import CommunicationLibraryInterface


# https://support.google.com/mail/answer/7126229?hl=en-GB is Google documentation on this

class Communication(CommunicationLibraryInterface):
    """The Communication Library of the project. Run through a sccdhuledTask or when called through the code."""

    def __init__(self, sent_from, password, url):
        """Method creating the Communication class"""
        self.sentFrom = sent_from
        self.password = password
        self.emailSmtp = 'smtp.gmail.com'
        self.portNumber = 465
        self.url = url

    def send_email(self, email_address, person_name, task_name, uuid):
        """Allows emails to be send regarding tasks being finished"""
        body = 'Dear ' + person_name + '.\n We can herby the task called ', task_name + "should be finished. Please " \
                                                                                        "Reply, King Regards, " \
                                                                                        "The system. " + self.url + \
               "/respond" + uuid + "/go "  # email message

        email_text = """\
   From: %s
   To: %s
   Subject: %s
   
   %s
      """ % (self.sentFrom, ", ".join(email_address), 'The task has been finished', body)  # Format f an email

        try:  # the process of sending a SMTP method. Might be a good idea to make this its own method in future.
            smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

            smtp_obj.ehlo()

            smtp_obj.login(self.sentFrom, self.password)  # Logins to the emails
            smtp_obj.sendmail(self.sentFrom, email_address, email_text)  # sends email
            print("Successfully sent email")  # ouput sucessful
        except smtplib.SMTPException:
            print("Error: unable to send email")  # error
