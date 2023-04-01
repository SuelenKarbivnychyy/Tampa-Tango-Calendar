from flask import Flask, Blueprint, request, render_template, session, redirect
from model import connect_to_db, db, Event, Location, Event_type
import crud                               
from datetime import datetime 
import send_email


admin_routing = Blueprint('admin_routing', __name__, template_folder='templates')

@admin_routing.route("/adm")
def display_adm_page():
    """Display events at the adm's page"""

    events_inf = Event.query.all()
    locations_inf = Location.query.all()
    events_type_inf = Event_type.query.all()
    user_id = session.get('current_user')        
    user_id_in_db = crud.get_user_by_id(user_id)
    
    if user_id == None:
        return redirect('/')
    elif user_id_in_db.is_adm == True:
        return render_template("adm.html", events_inf = events_inf, locations_inf = locations_inf, events_type_inf = events_type_inf)  
    else:
        return redirect('/')
    

@admin_routing.route("/add_event_type", methods=["POST"])
def add_event_type():
    """Add a new event type to the database"""

    event_name = request.form.get("event_name")
    new_event_title = crud.create_event_type(event_name)
    db.session.add(new_event_title)
    db.session.commit()   
    return redirect("/adm")


@admin_routing.route("/add_event_location", methods=["POST"])
def add_event_location(): 
    """Creating a new venue location"""   

    venue = request.form.get("venue_name")  
    address = request.form.get("venue_address") 
    city = request.form.get("venue_city")  
    state = request.form.get("venue_state") 
    zipcode = request.form.get("venue_zipcode")

    new_event_location = crud.create_location(venue, address, city, state, zipcode)       
    db.session.add(new_event_location)
    db.session.commit()
    return redirect("/adm")


@admin_routing.route("/add_event", methods=["POST"])
def add_event():
    """Add an event to the database"""

    event_start_date_time = request.form.get("event_start_date")      
    event_end_date_time = request.form.get("event_end_date")    
    event_description = request.form.get("description")    
    event_price = request.form.get("price")
    event_location_id = request.form.get("venues")
    event_type_id = request.form.get("type") 

    new_event = crud.create_event(start_date=event_start_date_time, end_date=event_end_date_time, description=event_description, price=event_price, location_id=event_location_id, event_type_id=event_type_id)
    db.session.add(new_event)
    db.session.commit()
    return redirect("/adm")


@admin_routing.route("/edit_event/<id>")
def edit_event(id):
    """Show edit event form"""  

    locations_inf = crud.get_all_location()
    events_type_inf = crud.get_all_events_type()    
    print(f"##############{id}")
    print(f"############# expression : {id == 'new'}")

    if id == "new":
        event = Event(id=-1, name="", description="", start_date_time=datetime.now(), end_date_time=datetime.now(), price=0)             #create a new instance of Event class
    else:
        event = crud.get_event_by_id(id) 
    return render_template("edit_event.html", event = event, locations_inf = locations_inf, events_type_inf = events_type_inf)
    

@admin_routing.route("/delete_event/<id>")
def delete_event(id):
    """This function checks if the event has reviews already, if does the reviews are deleted first then the event itself is Deleted."""   
    
    event_to_delete = crud.get_event_by_id(id) 
    event_reviews = crud.get_all_reviews_by_event_id(id)        
    for review in event_reviews:
        review_id = crud.get_review_by_id(review.id)
        db.session.delete(review_id)
        db.session.commit()
        
    db.session.delete(event_to_delete)
    db.session.commit() 
    return redirect("/adm")


@admin_routing.route("/update_event", methods=["POST"])
def check_event():
    """Check if event exists in database, update it if does, create a new event if does not."""
     
    form_event_id = request.form.get("event_id")                         # getting id from html form
    if form_event_id == "-1":
        print(f"#########{form_event_id}")
        event = Event()    
    else:                                                            # create a new event if id == -1
        event = crud.get_event_by_id(form_event_id)                 # passing the form id to the crud function

    event_name = request.form.get("event_name")
    event_description = request.form.get("description") 
    event_start_date = request.form.get("event_start_date")    
    event_end_date = request.form.get("event_end_date")       
    event_price = request.form.get("price")    
    event_location_id = request.form.get("venue")
    event_type_id = request.form.get("type")    

    event.name = event_name
    event.description = event_description
    event.start_date_time = event_start_date    
    event.end_date_time = event_end_date    
    event.price = event_price
    event.location_id = event_location_id
    event.event_type_id = event_type_id
    print(f"############ EVENT NAME: {event.name}")

    if event == -1:                                              # checking if the event being edit already in database add new event if does not exist in data base   
        print(f"event id : {event}")
        db.session.add(event)
        db.session.commit()
    elif event == event:
        db.session.add(event)                                        # and update it if does exists in data base
        db.session.commit()
    else:
        print("######### cancel")        
    return redirect("/adm")    


@admin_routing.route("/send_email", methods=["POST"])
def send_email_handler():
    """Function to send email to the users."""

    email_subject = "Tampa Tango Calendar updates."
    events = crud.get_all_events_type()
    email_message = (f"We are happy to send you our upcoming events, register yourself for: ")    

    for event in events:
        email_message += event.name + ", "   
    print(f"######## MESSAGE : {email_message}")

    users = crud.get_all_users()
    users_email = []
    for user in users:
        users_email.append(user.email)
    users_email = 'suelenmatosr@gmail.com';                         #this overrides the users_email list to be only one email.
     
    result = send_email.send_email_updates(users_email, email_subject, email_message)       #saving the result of send_email_updates function from send_email file
    if result == True:
        return "true"
    else:
        return "false"      
