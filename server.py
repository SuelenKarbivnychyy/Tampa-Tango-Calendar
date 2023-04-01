"""Server for Tango app."""
from flask import Flask, render_template
from model import connect_to_db
from jinja2 import StrictUndefined                      
from admin_blueprint import admin_routing
from event_blueprint import event_routing
from user_blueprint import user_routing

app = Flask(__name__)
app.register_blueprint(admin_routing)
app.register_blueprint(event_routing)
app.register_blueprint(user_routing)
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
