"""Server for Tango app."""

from flask import Flask, request, render_template, flash, session, redirect
from model import connect_to_db, db, Event, Location
from jinja2 import StrictUndefined                              #configure a Jinja2 setting to make it throw errors for undefined variables 

app = Flask(__name__)
app.app_context().push()

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route("/")
def homepage():
    """Render home page"""

    user = request.args.get('firstname')
    return render_template("homepage.html", name=user)


@app.route("/events")
def events_page():
    #read\query information from database
    # (as first attempt) put names of events to list
    # (as 2nd attempt)put it to list of dictionaries (or other data structure you want)
    # put that data to events template and in template read and render that data


    events_inf = Event.query.all()
    locations_inf = Location.query.all()
    # list_of_events = []

    # for event in events_inf:
    #     list_of_events.append(event)
        
    return render_template("events.html", events_inf = events_inf, locations_inf = locations_inf)  


@app.route("/adm")
def adm_page():

    return render_template("adm.html")     


@app.route("/subscribe")
def subscribe_page():

    return render_template("subscribe.html")        





if __name__ == "__main__":
    connect_to_db(app, "tango-project")                                       #connect to the database
    app.run(host="0.0.0.0", debug=True)
