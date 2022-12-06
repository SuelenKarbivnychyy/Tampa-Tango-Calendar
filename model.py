# pseudocode
# configure data base
# create tables 
# add relationship between tables


"""Model for Tango app"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Review(db.Model):
    """A Review"""

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    rate = db.Column(db.Integer, nullable = True)
    comment = db.Column(db.Text, nullable = True) 
    event_id = db.Column(db.Integer, db.ForeignKey('events.id')) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))                  

    event = db.relationship("Event", back_populates="reviews")
    user = db.relationship("User", back_populates="reviews")

    def __repr__(self):
        return f'<Id: {self.id} rate: {self.rate} comment: {self.comment}>'


class Event(db.Model):
    """An Event"""

    __tablename__ = 'events'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    name = db.Column(db.String)         
    description = db.Column(db.Text, nullable = False)                        
    start_date_time = db.Column(db.DateTime)    
    end_date_time = db.Column(db.DateTime)                    
    price = db.Column(db.Integer)                    
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    event_type_id = db.Column(db.Integer, db.ForeignKey('events_type.id'))    

    location = db.relationship("Location", back_populates="events")                             #specifing the relationship in between tables
    event_type = db.relationship("Event_type", back_populates="events")                         #specifing the relationship in between tables
    attendances = db.relationship("Attendance", back_populates="events")                        #specifing the relationship in between tables
    reviews = db.relationship("Review", back_populates="event")

    def __repr__(self):
        return f'<ID: {self.id} event_name: {self.name} duration: {self.duration} description: {self.description} date: {self.date} price: {self.price} location: {self.location.venue_name} event_type: {self.event_type.name}>'



class Event_type(db.Model):
    """A event type"""

    __tablename__ = 'events_type'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    name = db.Column(db.String, nullable = False)

    events = db.relationship("Event", back_populates="event_type")                       #specifing the relationship in between tables

    def __repr__(self):
        return f'<Event_type id={self.id} name={self.name}>'



class Location(db.Model):
    """A location"""

    __tablename__ = 'locations'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    venue_name = db.Column(db.String(50), nullable = False)                                     
    address = db.Column(db.Text, nullable = False)                        
    city = db.Column(db.String(25), nullable = False)                        
    state = db.Column(db.String(25), nullable = False)                    
    zipcode = db.Column(db.Integer, nullable = False)

    events = db.relationship("Event", back_populates="location")                        #specifing the relationship in between tables

    def __repr__(self):
        return f'<Venue: {self.venue_name} address: {self.address}>'



class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    fname = db.Column(db.String(25), nullable = False)                                     
    lname = db.Column(db.String(25), nullable = False)                        
    email = db.Column(db.String(50), unique = True, nullable = False)                        
    password = db.Column(db.String(30), nullable = False)                    
    is_adm = db.Column(db.Boolean, nullable = True)
   

    reviews = db.relationship("Review", back_populates="user")
    attendances = db.relationship("Attendance", back_populates="user")                  #specifing the relationship in between tables

    def __repr__(self):
        return f'<User id={self.id} fname={self.fname} lname={self.lname} email={self.email} password={self.password} adm={self.is_adm}>'



class Attendance(db.Model):
    """A attendence"""

    __tablename__ = 'attendances'

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    events = db.relationship("Event", back_populates="attendances")                      #specifing the relationship in between tables
    user = db.relationship("User", back_populates="attendances")                        #specifing the relationship in between tables

    def __repr__(self):
        return f'<Attendance_id={self.id} event_id={self.event_id} user_id={self.user_id}>' 




def connect_to_db(app, db_name):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")

 
 

if __name__ == "__main__":
    from server import app

    
    connect_to_db(app, "tango-project") 
