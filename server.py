"""Server for Tango app."""

from flask import Flask, request, render_template, flash, session, redirect, jsonify, flash
from model import connect_to_db, db, Event, Location, Event_type
import crud
from jinja2 import StrictUndefined                                 
from datetime import datetime 
import send_email 
from sqlalchemy import update

from admin_blueprint import admin_page
from event_blueprint import event_functionality_page
from user_blueprint import user_page

app = Flask(__name__)
app.register_blueprint(admin_page)
app.register_blueprint(event_functionality_page)
app.register_blueprint(user_page)
app.app_context().push()

app.secret_key = "tango"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def show_homepage():
    """Render home page"""    

    return render_template("homepage.html")


if __name__ == "__main__":
    connect_to_db(app, "tango-project")                                       #connect to the database
    app.run(host="0.0.0.0", debug=False)
