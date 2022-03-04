## The Scedulded Task file shall run reguarly. When it runs it will check the JSON File to check if task is due
import communication
import json
import datetime
from datetime import timedelta

theCurrentTime = datetime.datetime.now()  # gets current time
communicationObject = communication.Communication("hello@example.net", "hello", "http://127.0.0.1:5000/")


with open('members.json') as old_json_file:
    json_dict = json.load(old_json_file)  # opens the json file and converts it into a dictonary for python.

for people in json_dict:
    if theCurrentTime > (
            datetime.datetime.strptime((people["date"]), "%d/%m/%Y, %H:%M:%S") + timedelta(hours=people["hourstodo"])):
        # line above ^ once a certain amount people["hourstodo"] of hours has passed since the date was inputted
        communicationObject.send_email([people["email"]], people["name"], people["item"],
                                       people["uuid"])  # Conditon has been met for email notfication to be sent.
        print(people["date"], " with ", people["hourstodo"])
    else:
        print("not sent ", people["date"], " with ", people["hourstodo"])
