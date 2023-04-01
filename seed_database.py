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
model.db.create_all()                               #create database structure


#Load event data from json file
# SEEDING THE EVENT_TYPE TABLE
with open('data/events_type.json') as file:
    events_type= json.loads(file.read())
    

events_type_in_db = []
for event_type in events_type:
    name = event_type['name']   
    
    db_event_type = crud.create_event_type(name)
    events_type_in_db.append(db_event_type)

model.db.session.add_all(events_type_in_db)



##############################################################################################################################################
# SEEDING THE LOCATION TABLE

#Load movie data from json file
with open('data/events_location.json') as location_file:
    events_location_file= json.loads(location_file.read()) 

events_location_in_db = []
for event_location in events_location_file:
    venue_name = event_location['venue_name']  
    address = event_location['address']
    city = event_location['city']
    state = event_location['state']
    zipcode = event_location['zipcode']
    
    db_event_location = crud.create_location(venue_name, address, city, state, zipcode)
    events_location_in_db.append(db_event_location)



model.db.session.add_all(events_location_in_db)

###############################################################################################################################################
#SEED THE EVENT TABLE

with open('data/events.json') as events_file:
    events= json.loads(events_file.read()) 

events_in_db = []
for event in events:
    name = event['name']
    description = event['description']
    start_date_time = event['start_date_time']
    end_date_time = event['end_date_time']
    price = event['price']
    location_id = event['location_id']
    event_type_id = event['event_type_id']
    
    db_event = crud.create_event(name, description, start_date_time, end_date_time, price, location_id, event_type_id)
    events_in_db.append(db_event)



model.db.session.add_all(events_in_db)

############################################################################################################################################
#SEED THE ATTENDANCE TABLE


with open('data/events_attendance.json') as attendance_file:
    attendances= json.loads(attendance_file.read()) 

attendance_in_db = []
for attendance in attendances:
    event_id = attendance['event_id']  
    user_id = attendance['user_id']
 
    
    db_attendance = crud.create_attendance(event_id, user_id)
    attendance_in_db.append(db_attendance)

model.db.session.add_all(attendance_in_db)    

#######################################################################################################################################
#SEED THE REVIEW TABLE

with open('data/review.json') as review_file:
    reviews = json.loads(review_file.read())

reviews_in_db = []
for review in reviews:
    rate = review['rate']
    comment = review['comment']
    event_id = review['event_id']
    user_id = review['user_id']

    db_review = crud.create_review(rate, comment, event_id, user_id)
    reviews_in_db.append(db_review)

model.db.session.add_all(reviews_in_db)



# ###########################################################################################################################################
#GENERATE ACCOUNTS

with open('data/user_names.json') as user_file:
    users_name = json.loads(user_file.read())

users_information_in_db = []
n = 1
for name in users_name:
    fname = name["first_name"]
    lname = name["last_name"]
    email = f"suelenmatosr+{n}@gmail.com"
    password = "test"
    is_adm = False
    n += 1    

    user = crud.create_user(fname, lname, email, password, is_adm)  
    users_information_in_db.append(user)
    model.db.session.add_all(users_information_in_db)   


adm = crud.create_user('Suelen', 'Matos', 'suelenmatosr@outlook.com', '123', True )
model.db.session.add(adm)
model.db.session.commit()                                               #COMMIT TO THE DATABASE AT THE VERY END TO AVOID COMMIT ALL THE TIME YOU ADD NEW INF TO THE DATABASE