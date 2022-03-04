import smtplib
from pushbullet import Pushbullet


## The Communication Library of the project. Run through a sccdhuledTask or when called through the code.


def send_push_notification(message):
    api_key = "o.UINgqIWYaGd9m0s43C3W0CjOinoaANzu"

    push_bullet = Pushbullet(api_key)
    push = push_bullet.push_note("Notification from the Human Program", message)


class Communication:
    def __init__(self, sent_from, password, url):
        self.sentFrom = sent_from
        self.password = password
        self.emailSmtp = 'smtp.gmail.com'
        self.portNumber = 465
        self.url = url

    def send_email(self, email_address, person_name, task_name,
                   uuid):  # the method that sends emails as describied in What has been done so far with Communication Library
        to = email_address
        subject = 'The task has been finished'
        body = 'Dear ' + person_name + '.\n We can herby the task called ', task_name + "should be finished. Please Reply, King Regards, The system. " + self.url + "/respond" + uuid + "/go"

        email_text = """\
   From: %s
   To: %s
   Subject: %s
   
   %s
      """ % (self.sentFrom, ", ".join(to), subject, body)

        try:
            smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

            smtp_obj.ehlo()

            smtp_obj.login(self.sentFrom, self.password)
            smtp_obj.sendmail(self.sentFrom, to, email_text)
            print("Successfully sent email")
        except smtplib.SMTPException:
            print("Error: unable to send email")
