"""CRUD operations."""

from model import db, Event, Event_type, Location, User, Attendance, connect_to_db



def create_user(fname, lname, email, password):
    """Create and return a new user."""

    user = User(fname=fname,
                lname=lname,
                email=email,
                password=password)

    return user


def get_user_by_email(email):                       #return a user with that email if exists, return none otherwise
    """Return a user by email."""
    

    return User.query.filter(User.email == email).first()   

    
    







def create_event(duration, description, date, price, location_id, event_type_id):           #figure it out how to add the location and the event type
    """Creat and return an event"""

    event = Event(duration=duration,
                description=description, 
                date=date,
                price=price,
                location_id=location_id,
                event_type_id=event_type_id)

    return event


def get_event_by_id(id):                                               
    """Return events by id"""

    return Event.query.get(id)  


def get_all_events():                                               #getting all events from database
    """Return all events"""
    
    return Event.query.all()





def create_event_type(name):
    """Create and return an event type"""

    event_type = Event_type(name=name)    

    return event_type

def get_all_events_type():
    """Return all events type"""
    
    return Event_type.query.all()







def create_location(venue_name, address, city, state, zipcode): 
    """Create and return a location"""

    location = Location(venue_name=venue_name,
                        address=address, 
                        city=city,
                        state=state, 
                        zipcode=zipcode )

    return location

def get_location(id):
    """Return location by id"""

    return Location.query.get(id)

def get_all_location():
    """Return all locations"""

    return Location.query.all()


# figure out about attendance table

def create_attendance(event_id, user_id):
    """Create and return a attendance"""

    attendance = Attendance(event_id=event_id,
                            user_id=user_id)

    return attendance                        



def get_attendance(event_id, user_id):
    """Return an attendance"""

    return Attendance.query.filter(Attendance.event_id == event_id, Attendance.user_id == user_id).first()


def get_all_attendance():

    return Attendance.query.all()







# def create_a_subscribe(email):
#     """Create and return a subscriber user"""

#     email_to_subscribe = Subscribe()







if __name__ == '__main__':
    from server import app
    connect_to_db(app, "tango-project")