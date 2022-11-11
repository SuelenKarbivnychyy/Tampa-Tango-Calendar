"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model 
import server
from model import Event_type

os.system('dropdb tango-project')
os.system('createdb tango-project')

model.connect_to_db(server.app, "tango-project")
model.db.create_all()


#Load movie data from json file
with open('data/events_type.json') as file:
    events_type= json.loads(file.read())
    # print(f"####################### THIS IS THE EVENTS TYPE FROM JSON FILE {events_type}")

events_type_in_db = []
for event_type in events_type:
    name = event_type['name']   
    # print(f"############################## THIS IS THE EVENT NAME{name}")
    db_event_type = crud.create_event_type(name)
    events_type_in_db.append(db_event_type)

# print(f"################################## THE LIST AFTER APPEND {events_type_in_db}")

model.db.session.add_all(events_type_in_db)
model.db.session.commit()
# print(f"################################## AFTER COMMIT {events_type_in_db}")


##############################################################################################################################################