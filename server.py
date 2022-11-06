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



























# @app.route("/adm")
# def adm_page():

#     events_inf = Event.query.all()
#     locations_inf = Location.query.all()
#     events_type_inf = Event_type.query.all()
#     return render_template("adm.html", events_inf = events_inf, locations_inf = locations_inf, events_type_inf = events_type_inf)     


# @app.route("/subscribe")
# def subscribe_page():

#     return render_template("subscribe.html")        





if __name__ == "__main__":
    connect_to_db(app, "tango-project")                                       #connect to the database
    app.run(host="0.0.0.0", debug=True)
