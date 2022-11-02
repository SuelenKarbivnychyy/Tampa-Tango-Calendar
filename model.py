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
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_type.id'))

    def __repr__(self):
        return f'<Event id={self.id} duration={self.duration} description={self.description}>'



class Events_type(db.Model):
    """A event type"""

    __tablename__ = 'event_type'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'<Event_type id={self.id} name={self.name}>'



class Locations(db.Model):
    """A location"""

    __tablename__ = 'location'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    venue_name = db.Column(db.String(25))                                     
    address = db.Column(db.Text(50))                        
    city = db.Column(db.String(25))                        
    state = db.Column(db.String(25))                    
    zipcode = db.Column(db.Integer)

    def __repr__(self):
        return f'<Locations id={self.id} venue_name={self.venue_name} address={self.address}>'



class Users(db.Model):
    """A user"""

    __classname__ = 'user'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    fname = db.Column(db.String(25))                                     
    lname = db.Column(db.String(25))                        
    email = db.Column(db.String(50), unique = True)                        
    password = db.Column(db.String(30))                    
    is_adm = db.Column(db.Boolean)

    def __repr__(self):
        return f'<User id={self.id} fname={self.fname} lname={self.lname} email={self.email}>'



class Attendances(db.Model):
    """A attendence"""

    __tablename__ = 'event_type'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return f'<Event_type id={self.id} name={self.name}>'        




                                                                                                  













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