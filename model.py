# ''' Model for Tango app'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Event(db.Model):
    """An Event"""

    __tablename__ = 'events'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    duration = db.Column(db.Integer)                                     
    description = db.Column(db.Text)                        
    date = db.Column(db.DateTime)                        
    price = db.Column(db.Integer)                        
    duration = db.Column(db.Integer)                        
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_type.id'))
                                                                                                  













def connect_to_db(app, db_name):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

 
 

if __name__ == "__main__":
    from server import app

    connect_to_db(app, "tango-final-project")    











# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# # create the extension
# db = SQLAlchemy()
# # create the app
# app = Flask(__name__)
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tango-final-project"
# # initialize the app with the extension
# db.init_app(app)
# db.create_all()