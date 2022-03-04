import json
import datetime
from datetime import timedelta
import os
import uuid

from markupsafe import string


def change_task(unique_id, answer):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    memberFile = os.path.join(THIS_FOLDER, 'members.json')

    with open(memberFile) as json_file:
        json_dict = json.load(json_file)
    for event in json_dict:
        if event["uuid"] == unique_id:
            event["hourstodo"] = int(event["hourstodo"]) + 5
            break
    new_json_file = json.dumps(json_dict)
    with open(memberFile, 'w') as outfile:
        outfile.write(new_json_file)


def add_new_task(email, personName, mission, timealloted):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    member_file = os.path.join(THIS_FOLDER, 'members.json')

    the_current_time = datetime.datetime.now()
    the_current_time_string = the_current_time.strftime("%d/%m/%Y, %H:%M:%S")

    with open(member_file) as json_file:
        json_dict = json.load(json_file)

    uniqueIDNumber = uuid.uuid4()
    newTask = {
        "uuid": str(uniqueIDNumber),
        "email": email,
        "name": personName,
        "date": the_current_time_string,
        "item": mission,
        "hourstodo": str(timealloted)
    }
    json_dict.append(newTask)
    new_json_file = json.dumps(json_dict)
    with open(member_file, 'w') as outfile:
        outfile.write(new_json_file)


