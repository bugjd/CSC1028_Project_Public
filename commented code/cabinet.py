import json
import datetime
from datetime import timedelta
import os
import uuid

from markupsafe import string


def change_task(unique_id, answer):
    """Allows tasks to be changed"""
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))  # Finds the folder your in on your system
    memberFile = os.path.join(THIS_FOLDER, 'members.json')  # finds the exact location of the members,sjon file

    with open(memberFile) as json_file:  # tries to open the file
        json_dict = json.load(json_file)
    for event in json_dict:
        if event["uuid"] == unique_id:
            event["hourstodo"] = int(event["hourstodo"]) + 5  # makes the edit
            break
    new_json_file = json.dumps(json_dict)
    with open(memberFile, 'w') as outfile:  # over writes the file
        outfile.write(new_json_file)


def add_new_task(email, person_name, mission, allotted):
    """Adds new tasks to the JSON File"""
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))  # Finds the folder your in on your system
    memberFile = os.path.join(THIS_FOLDER, 'members.json')  # finds the exact location of the members,sjon file

    the_current_time = datetime.datetime.now()
    the_current_time_string = the_current_time.strftime("%d/%m/%Y, %H:%M:%S")

    with open(memberFile) as json_file:  # tries to open the file
        json_dict = json.load(json_file)

    uniqueIDNumber = uuid.uuid4() # creates a unique id.
    newTask = { # creates a dictionary of the content to go into the JSON file
        "uuid": str(uniqueIDNumber),
        "email": email,
        "name": person_name,
        "date": the_current_time_string,
        "item": mission,
        "hourstodo": str(allotted)
    }
    json_dict.append(newTask) # adds the new task to the json fole
    new_json_file = json.dumps(json_dict)
    with open(memberFile, 'w') as outfile: # overwrites the old file
        outfile.write(new_json_file)
