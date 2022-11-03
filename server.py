"""Server for Tango app."""

from flask import Flask, request, render_template

app = Flask(__name__)
app.app_context().push()


# Replace this with routes and view functions!
@app.route("/login")
def login_page():
    """Render login page"""

    user = request.args.get('firstname')
    return render_template("login.html", name=user)

@app.route("/events")
def events_page():

    return render_template("events.html")    

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
