"""Server for Tango app."""

from flask import Flask, request, render_template, flash, session, redirect, jsonify
from model import connect_to_db, db, Event, Location, Event_type
import crud
from jinja2 import StrictUndefined                              #configure a Jinja2 setting to make it throw errors for undefined variables 

app = Flask(__name__)
app.app_context().push()

app.secret_key = "tango"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
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
    else:     
        return render_template("homepage.html")
  


@app.route("/events")
def all_events():
    """View all events"""
    #read\query information from database
    # (as first attempt) put names of events to list
    # (as 2nd attempt)put it to list of dictionaries (or other data structure you want)
    # put that data to events template and in template read and render that data    
    
    event_type = crud.get_event_type()
    return render_template("events.html", event_type = event_type)


@app.route("/events/<id>")    
def show_event(id):
    """View event detail"""

    location = crud.get_location(id)
    event = crud.get_event_by_id(id)
    return render_template("events_details.html", event = event, location = location)



#create the receiver API POST endpoint:
@app.route("/check_email", methods=["POST"])
def check_email():
    """Check if user in db"""    
   
    email_from_input = request.json.get("email")                                      #information from browser
    password = request.json.get("password")
    # print(f" ################################## {email}")
    # print(f" @@@@@@@@@@@@@@@@@@@ {password}")


    user_db = crud.get_user_by_email(email_from_input)                   #checking if the user's email input from the browser has any matchs at the database
    if user_db == None :                                                 #checking if user is not in db and return "no results if true"
        # print("##########")                                            #test
        return "no result"

    user_password = user_db.password                                      #getting the password from db's user if there is a match

    if user_password == password:                                         #giving access to user is informations macth
        return "welcome"
    else:
        return "incorrect email or password"                              #trowing an error other wise
    


@app.route("/create_account") 
def create_account():
    """Create an user account"""   

    return render_template("create_account.html")  



@app.route("/add_user_to_db", methods=["POST"]) 
def add_account():
    """Add an user account to database"""   

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    email = request.form.get("email")
    password = request.form.get("password")

    new_user = crud.create_user(first_name, last_name, email, password)
    db.session.add(new_user)
    db.session.commit()

    # print(new_user) test
    # print(f"############### {first_name}, {last_name}, {email}, {password}") test
    return redirect("/")  




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


@app.route("/add_event", methods=["POST"])
def add_event():
    """Add a event to the database"""

    event_date = request.form.get("event_date")  
    event_description = request.form.get("description")    
    event_price = request.form.get("price")
    event_duration = request.form.get("event_duration")

    new_event = crud.create_event(event_date, event_description, event_price, event_duration)

    db.session.add(new_event)
    db.session.commit()

    return redirect("/adm")
    # return render_template("/adm.html", event_date = event_date,
    #                                     description = event_description,
    #                                     price = event_price,
    #                                     event_duration= event_duration)    









# @app.route("/subscribe")
# def subscribe_page():

#     return render_template("subscribe.html")        





if __name__ == "__main__":
    connect_to_db(app, "tango-project")                                       #connect to the database
    app.run(host="0.0.0.0", debug=True)
