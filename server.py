"""Server for Tango app."""

from flask import Flask, request, render_template, flash, session, redirect, jsonify
from model import connect_to_db, db, Event, Location, Event_type
import crud
from jinja2 import StrictUndefined                                   #configure a Jinja2 setting to make it throw errors for undefined variables
from datetime import datetime                             

app = Flask(__name__)
app.app_context().push()

app.secret_key = "tango"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """Render home page"""    

    identify = request.args.get("/homepage")

    if identify == 'events':
        return redirect("events")
    elif identify == 'subscribe':
        return redirect("subscribe")  
    elif identify == 'adm':
        return redirect("adm") 
    elif identify == "user_profile":
        return redirect("user_profile")                       
    else:     
        return render_template("homepage.html")


# @app.route("/user_profile")
# def user_profile():
#     """Display user's profile"""

#     return render_template("user_profile.html")   


@app.route("/event_attendance", methods=["POST"])
def count_attendance():
    """Display the attendance for an event"""
   

    event_id = request.json.get("event_id")
    user_id = session['current_user']

    check_attendance = crud.get_attendance(event_id, user_id)
    # print(f"############################### I'M THE event id and user id: {check_attendance}")            test
    

    if check_attendance == None:
        # print("##################### I'M IN DATA BASE")
        add_attendance = crud.create_attendance(event_id, user_id)
        db.session.add(add_attendance)        
        db.session.commit()
        print(f"############ ADDED TO DATABASE {event_id} {user_id}")
        return "added to db"
    else:
        return "I'm in database already"







####################################################################

@app.route("/events")
def all_events():
    """View all events"""
    #read\query information from database
    # put that data to events template and in template read and render that data    
    
    # list_of_events= crud.get_all_events()
    list_of_attendance = crud.get_all_attendance() #getting all the attendance for events
    print(f"EVENTS LIST ##################### {list_of_attendance}")
    return render_template("events.html", list_of_attendance=list_of_attendance)


@app.route("/events/<id>")    
def show_event(id):
    """View event details"""
  
    event = crud.get_event_by_id(id)
    return render_template("events_details.html", event = event)



#create the receiver API POST endpoint:
@app.route("/validate_user_credentials", methods=["POST"])
def validate_user_credentials():           
    """Check if user's credential are correct to login"""    
   
    email_from_input = request.json.get("email")                                      #information from browser as json
    password = request.json.get("password")
    # print(f" ################################## {email}, {password}")

    user_db = crud.get_user_by_email(email_from_input)                      #checking if the user's email input from the browser has any matchs at the database
    if user_db == None :                                                    #checking if user is not in db and return "no results if true"
        # flash("create an account")
        return "no result"

    user_id= user_db.id
    user_password = user_db.password                                        #getting the password from db's user if there is a match
    if user_password == password:                                           #giving access to user if informations macth
        session['current_user'] = user_id
        print(f"#############################{user_id}")                  #test
        # flash(f"Logged in as {user_db.fname, user_db.lname}")
        return "true"
    else:
        # flash("incorrect email or password")
        return "false"


    

#pseudocode
# create a route function to check if email is in data base
# for the purpose of telling user if he already has an account
# on the create account feature

@app.route("/validate_email", methods=["POST"])
def validate_email():
    """Validate email to create an account"""

    email = request.json.get("email")
    user = crud.get_user_by_email(email)

    if user != None:
        return "true"
    else:
        return "false"


@app.route("/create_account") 
def create_account():
    """Render create account template"""   

    return render_template("create_account.html") 

#Route to submit the form
@app.route("/add_user_to_db", methods=["POST"])                              #route to submit the form
def add_account():
    """Add an user account to database (create account)"""   

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    email = request.form.get("email")
    password = request.form.get("password") 

    new_user = crud.create_user(first_name, last_name, email, password)
    db.session.add(new_user)
    db.session.commit()
        # print(new_user)                                                    #test
  
    return redirect("/")  


##########################################################################################################################
# ADM BUSINESS STARTS FROM HERE  

@app.route("/adm")
def adm_page():
    """Display events at the adm's page"""

    events_inf = Event.query.all()
    locations_inf = Location.query.all()
    events_type_inf = Event_type.query.all()
    return render_template("adm.html", events_inf = events_inf, locations_inf = locations_inf, events_type_inf = events_type_inf)  
    



@app.route("/add_event_type", methods=["POST"])
def add_event_type():
    """Add a new event type to the database"""

    event_name = request.form.get("event_name")
    # print(f"########################### {event_name}")            #test

    new_event_title = crud.create_event_type(event_name) 

    db.session.add(new_event_title)
    db.session.commit()
   
    # return render_template("/adm.html", event_name = event_name)
    return redirect("/adm")



@app.route("/add_event_location", methods=["POST"])
def add_event_location():                                        

    venue = request.form.get("venue_name")  
    address = request.form.get("venue_address") 
    city = request.form.get("venue_city")  
    state = request.form.get("venue_state") 
    zipcode = request.form.get("venue_zipcode")                                

    new_event_location = crud.create_location(venue, address, city, state, zipcode)
   
    db.session.add(new_event_location)
    db.session.commit()

    # print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ {new_event_location}")              #test
    return redirect("/adm")


@app.route("/add_event", methods=["POST"])                                      #adding a new event to the data base
def add_event():
    """Add a event to the database"""

    event_date = request.form.get("event_date")  
    event_description = request.form.get("description")    
    event_price = request.form.get("price")
    event_duration = request.form.get("event_duration")
    event_location_id = request.form.get("venues")
    event_type_id = request.form.get("type")
 

    new_event = crud.create_event(date=event_date, description=event_description, price=event_price, duration=event_duration, location_id=event_location_id, event_type_id=event_type_id)
    print(f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%{new_event}")
    db.session.add(new_event)
    db.session.commit()

    return redirect("/adm")
    # return render_template("/adm.html", event_date = event_date,
    #                                     description = event_description,
    #                                     price = event_price,
    #                                     event_duration= event_duration)    


@app.route("/edit_event/<id>")
def edit_event(id):
    """Show edit event form"""

    # events_inf = Event.query.all()
    locations_inf = crud.get_all_location()
    events_type_inf = crud.get_all_events_type()    
    print(f"######################################{id}")
    print(f"###################################### expression : {id == 'new'}")

    if id == "new":
        event = Event(id=-1, duration=0, description="", date=datetime.now(), price=0)             #create a new instance of Event class
        # print(f"********Babe's event {event}")                                                   #test                                 
    else:
        event = crud.get_event_by_id(id)   

    return render_template("edit_event.html", event = event, locations_inf = locations_inf, events_type_inf = events_type_inf)
    

@app.route("/delete_event/<id>")
def delete_event(id):
    """Delete a event"""
   
    event_to_delete = crud.get_event_by_id(id) 
    db.session.delete(event_to_delete)
    db.session.commit()

    return redirect("/adm")

@app.route("/update_event", methods=["POST"])
def check_event():
    """Check if event exists in database"""

     
    form_event_id = request.form.get("event_id")                # getting id from html form
    if form_event_id == "-1":
        print(f"#######################{form_event_id}")
        event = Event()    
    else:                                         # create a new event if id == -1
        event = crud.get_event_by_id(form_event_id)                 # passing the form id to the crud function


    event_duration = request.form.get("event_duration")
    event_description = request.form.get("description") 
    event_date = request.form.get("event_date")      
    event_price = request.form.get("price")    
    event_location_id = request.form.get("venue")
    event_type_id = request.form.get("type")
    print(f" EVENT LOCATION { event_location_id }")
    print(f" EVENT TYPE ID {event_type_id}")

    event.duration = event_duration
    event.description = event_description
    event.date = event_date
    event.price = event_price
    event.location_id = event_location_id
    event.event_type_id = event_type_id

    if event != None:                                       #checking if the event being edit already in database and update it if does
        db.session.add(event)
        db.session.commit()
    elif event == event:
        db.session.add(event)                               # add new event if does not exist in data base
        db.session.commit()
    else:
        print("############################### cancel")        

    print(f"UPDATED EVENTS #####################{event}")

    # print(date=event_date, description=event_description, price=event_price, duration=event_duration, location_id=event_location_id, event_type_id=event_type_id)

    return redirect("/adm")    


    






# @app.route("/subscribe")
# def subscribe_page():
#     """Subscribe user to automatic email recieve"""

#     return render_template("subscribe.html")   

# @app.route("/add_subscribe_user")         
# def subscribe_user():
#     """Add subscribe user to database"""

#     email_subscribe = request.form.get("subscribe")


#     return redirect("/")





if __name__ == "__main__":
    connect_to_db(app, "tango-project")                                       #connect to the database
    app.run(host="0.0.0.0", debug=True)
