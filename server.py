"""Server for Tango app."""

from flask import Flask, request, render_template, flash, session, redirect, jsonify, flash
from model import connect_to_db, db, Event, Location, Event_type
import crud
from jinja2 import StrictUndefined                                   #configure a Jinja2 setting to make it throw errors for undefined variables
from datetime import datetime 
import send_email                            

app = Flask(__name__)
app.app_context().push()

app.secret_key = "tango"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """Render home page"""    

    # identify = {'events' : 'events', 'adm' : 'adm', 'user_profile': 'user_profile'}

    identify = request.args.get("/homepage")

    if identify == 'events':
        return redirect("events")     
    elif identify == 'adm':
        return redirect("adm") 
    elif identify == "user_profile":
        return redirect("user_profile")                       
    else:     
        return render_template("homepage.html")



@app.route("/event_sign_in", methods=["POST"])
def count_attendance():
    """Display the attendance for the events"""    

    event_id = request.json.get("event_id")
    user_id = session.get('current_user')

    if user_id == None:                                                                                  #if user not in session it will not allows user to sign in for event
        print(user_id)
        return "Please login."

    check_attendance = crud.get_attendance(event_id, user_id)
    # print(f"############################### I'M THE event id and user id: {check_attendance}")           #test
    
    if check_attendance == None:       
        # print("##################### I'M IN DATA BASE")                                                  #test
        add_attendance = crud.create_attendance(event_id, user_id)
        db.session.add(add_attendance)        
        db.session.commit()
        print(f"############ ADDED TO DATABASE {event_id} {user_id}")
        return "You are sucessfully sign in for this event."
    else:
        return "You are already sign in for this event."


@app.route("/sign_out", methods=["POST"])    
def cancel_user_attendance():
    """Cancel user attendance to an event"""   

    event_id = request.json.get("event_id")
    # print(f"######### EVENT ID FROM SIGN OUT ROUT {event_id} %%%%%%%%%%%%")
    user_id = session['current_user'] 
    check_attendance = crud.get_attendance(event_id, user_id)

    if check_attendance != None: 
        db.session.delete(check_attendance)
        db.session.commit()
        return "You are signed out for this event. We are sorry to let you go."
    else:
        return "You've signed out."      



@app.route("/events")
def all_events():
    """View all events"""


    events = crud.get_all_events()
    # print(f"############ events {events}")

    rate = {}    
    for event in events:
        counter = 0
        for review in event.reviews:
            total_review_per_event = len(event.reviews)
            counter += review.rate
            rate[event.id] = counter / total_review_per_event
    print(f"############### reviews rate: {rate}")

    
    list_of_attendance = crud.get_all_attendance()
    # print(f"############ LIST OF ATTENDANCE {list_of_attendance}")
    # print(f" ################## all events: {events}")
    user_id = session.get("current_user")
    # print(f"########################## ID IN SESSION {user_id}")

    current_user_events={}

    if user_id != None:    
        attendances = crud.get_all_attendance_for_a_user(user_id)  
        for attendance in attendances:
            current_user_events[attendance.event_id] = "true"
    # print(f"########################## DICTIONARY WITH EVENTS USER IS GOING TO {current_user_events}") 

    return render_template("events.html", events=events,
                                        attendances=current_user_events,
                                        attendance_number = list_of_attendance,
                                        rate=rate
                                        )


@app.route("/events/<id>")    
def show_event_details(id):
    """View event details"""

    user = session.get("current_user")
    # print(f"####### user id {user}")
    event = crud.get_event_by_id(id)
    review = crud.get_review_by_event_and_user(event.id, user)
    # print(f"######################### review {review}")
    reviews_db = crud.get_all_reviews_by_event_id(event.id)
    
    return render_template("events_details.html", event = event, review = review, reviews_db = reviews_db)


@app.route("/review", methods=["POST"])
def make_review():
    """Create an review"""
    
    #pseudocode
    #get user in session
    #get event id
    #get rate and review using json.get
    #check if event already have an review from this user
    #add it to the databe if dont

    event_id = request.json.get('event_id')
    # print(f"################################### event id in python: {event_id}")
    user_id = session.get('current_user')    
    user_rate = request.json.get("user_rate")
    # print(f"####### user rate python: {user_rate}")
    user_review = request.json.get("user_review")
    # print(f"################## user review: {user_review}")
    review_from_db = crud.get_review_by_event_and_user(event_id, user_id)
    print(f"############# review from db: {review_from_db}")

    if review_from_db == None:    
        new_review = crud.create_review(user_rate, user_review, event_id, user_id)
        db.session.add(new_review)
        db.session.commit()
        return "true"
    else:
        print(f"################## review {review_from_db.comment}")
        return "false"



@app.route("/delete_review", methods=["POST"])
def delete_review():
    """Delete a review"""

    #pseudocode
    #get event id and user id
    #check if has a review in data base with that event id and user id
    #delete event if it does

    user_id = session.get('current_user')  
    event_id = request.json.get('event_id')
    review_id = request.json.get('review_id')
    review_in_db = crud.get_review_by_id(review_id)
    
    print(f"############################# review id: [{review_in_db}]")
    if review_in_db != None:
        db.session.delete(review_in_db)
        db.session.commit()
        return "Review deleted"
    else:
        return "deleted"    





################################################################################################################################################



#create the receiver API POST endpoint:
@app.route("/validate_user_credentials", methods=["POST"])
def validate_user_credentials():           
    """Check if user's credential are correct to login"""    
   
    email_from_input = request.json.get("email")                                      #information from browser as json
    password = request.json.get("password")
    # print(f" ################################## {email}, {password}")

    user_db = crud.get_user_by_email(email_from_input)                      #checking if the user's email input from the browser has any matchs at the database
    
    if user_db == None :                                                    #checking if user is not in db and return "no results if true"
        # flash("Account does not existe. create an account")        
        return "no result"  
   
    user_id= user_db.id
    user_password = user_db.password                                        #getting the password from db's user if there is a match
    if user_password == password:                                           #giving access to user if informations macth
        session['current_user'] = user_id
        session["user_name"]= f"{user_db.fname} {user_db.lname}"            #setting first name and last name from session
        
        is_administrator = user_db.is_adm
        session["is_adm"]= is_administrator  
        print(f"################# adm information {is_administrator}")      
        # print(f"#############################{user_id}")                    #test
        return "true"
    else:
        return "false"


@app.route("/logout")
def lougout():        
    session.pop('user_name')
    session.pop('current_user')
    session.pop('is_adm')

    return redirect('/')


    

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




@app.route("/user_profile")
def user_profile():
    """Display user's profile"""

    # user = session["current_user"]                                                          #getting user id from session
    # print(f"################ user id from session: {user}")
    user = session.get("current_user")
    print(f"####################### USER IN SESSION: {user}")
    if user == None:
        return redirect('/')

    attendances = crud.get_all_attendance_for_a_user(user)                                 #returning a list
    events = []
    print(f"##############################ATTENDNACES: {attendances}")
    # print(f"########### EVENTS: {events}")
    
    for attendance in attendances:
        events.append(attendance.events)
    print(f"################# EVENTS THE USER IS SIGN IN FOR: {events}")

    user_reviews = crud.get_all_reviews_for_a_user(user)
    reviews = []

    for review in user_reviews:
        reviews.append(review)
    # print(f"########################## REVIEWS: {reviews}")    

    return render_template("/user_profile.html", events=events, reviews=reviews)











##########################################################################################################################
# ADM BUSINESS STARTS FROM HERE  

@app.route("/adm")
def adm_page():
    """Display events at the adm's page"""

    events_inf = Event.query.all()
    locations_inf = Location.query.all()
    events_type_inf = Event_type.query.all()

    user_id = session.get('current_user')
    # print(f"####### user in session {user_id}")                       #test
    
    user_id_in_db = crud.get_user_by_id(user_id)
    # print(f"######### database {user_id_in_db}")                     #test

    if user_id == None:
        return redirect('/')
    elif user_id_in_db.is_adm == True:
        return render_template("adm.html", events_inf = events_inf, locations_inf = locations_inf, events_type_inf = events_type_inf)  
    else:
        return redirect('/')



@app.route("/add_event_type", methods=["POST"])
def add_event_type():
    """Add a new event type to the database"""

    event_name = request.form.get("event_name")
    print(f"########################### {event_name}")            #test

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

    event_start_date_time = request.form.get("event_start_date")  
    print(f"##################### START TIME DATE {event_start_date_time}")
    event_end_date_time = request.form.get("event_end_date")
    print(f"##################### end TIME DATE {event_end_date_time}")
    event_description = request.form.get("description")    
    event_price = request.form.get("price")
    event_location_id = request.form.get("venues")
    event_type_id = request.form.get("type")
 

    new_event = crud.create_event(start_date=event_start_date_time, end_date=event_end_date_time, description=event_description, price=event_price, location_id=event_location_id, event_type_id=event_type_id)
    print(f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%{new_event}")
    db.session.add(new_event)
    db.session.commit()

    return redirect("/adm")
     


@app.route("/edit_event/<id>")
def edit_event(id):
    """Show edit event form"""

    # events_inf = Event.query.all()
    locations_inf = crud.get_all_location()
    events_type_inf = crud.get_all_events_type()    
    print(f"######################################{id}")
    print(f"###################################### expression : {id == 'new'}")

    if id == "new":
        event = Event(id=-1, name="", description="", start_date_time=datetime.now(), end_date_time=datetime.now(), price=0)             #create a new instance of Event class
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

     
    form_event_id = request.form.get("event_id")                         # getting id from html form
    if form_event_id == "-1":
        print(f"#######################{form_event_id}")
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
    # print(f" EVENT LOCATION { event_location_id }")
    # print(f" EVENT TYPE ID {event_type_id}")

    event.name = event_name
    event.description = event_description
    event.start_date_time = event_start_date
    # print(f"#########################3 EVENT START: {event.start_date_time}") 
    event.end_date_time = event_end_date
    # print(f"#################### EVENT END {event.end_date_time}")
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
        print("############################### cancel")        
    return redirect("/adm")    


@app.route("/send_email", methods=["POST"])
def send_email_handler():

    email_subject = "Tampa Tango Calendar updates."
    events = crud.get_all_events_type()
    email_message = (f"We are happy to send you our upcoming events, Register yourself for: ")
    
    for event in events:
        email_message += event.name + ", "   
    print(f"######## MESSAGE : {email_message}")

    users = crud.get_all_users()
    users_email = []

    for user in users:
        users_email.append(user.email)

    users_email = 'suelenmatosr@gmail.com';                         #this overrides the users_email list to be only one email.

    # print(f"############### ALL USERS email: {users_email}")   

    result = send_email.send_email_updates(users_email, email_subject, email_message)

    if result == True:
        return "true"
    else:
        return "false"    



if __name__ == "__main__":
    connect_to_db(app, "tango-project")                                       #connect to the database
    app.run(host="0.0.0.0", debug=True)
