"""Server for Tango app."""

from flask import Flask, request, render_template, flash, session, redirect
from model import connect_to_db, db, Event, Location, Event_type
from jinja2 import StrictUndefined                              #configure a Jinja2 setting to make it throw errors for undefined variables 

app = Flask(__name__)
app.app_context().push()

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route("/")
def homepage():
    """Render home page"""
    

    identity = request.args.get("/homepage")

    if identity == 'events':
        return redirect("events")
    elif identity == 'subscribe':
        return redirect("subscribe")  
    elif identity == 'adm':
        return redirect("adm") 
    elif identity == 'login':
        return redirect("login")               
    else:     
        return render_template("homepage.html")

    # return redirect("/")    


@app.route("/login")
def login():
    """Login page"""

    user = request.args.get('firstname')
    return render_template("login.html", name = user)    


@app.route("/events")
def events_page():
    #read\query information from database
    # (as first attempt) put names of events to list
    # (as 2nd attempt)put it to list of dictionaries (or other data structure you want)
    # put that data to events template and in template read and render that data


    events_inf = Event.query.all()
    locations_inf = Location.query.all()
    events_type_inf = Event_type.query.all()
        
    return render_template("events.html", events_inf = events_inf, locations_inf = locations_inf, events_type_inf = events_type_inf)  



@app.route("/adm")
def adm_page():

    events_inf = Event.query.all()
    locations_inf = Location.query.all()
    events_type_inf = Event_type.query.all()
    return render_template("adm.html", events_inf = events_inf, locations_inf = locations_inf, events_type_inf = events_type_inf)     


@app.route("/subscribe")
def subscribe_page():

    return render_template("subscribe.html")        





if __name__ == "__main__":
    connect_to_db(app, "tango-project")                                       #connect to the database
    app.run(host="0.0.0.0", debug=True)
