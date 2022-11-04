"""CRUD operations."""

from model import db, Event, Event_type, Location, User, Attendance, connect_to_db



def create_user(fname, lname, email, password):
    """Create and return a new user."""

    user = User(fname=fname,
                lname=lname,
                email=email,
                password=password)

    return user


def get_user_by_email(email):                       #return a user with that email of exists, return none otherwise
    """Return a user by email."""    

    return User.query.filter(User.email == email).first()   
    







def create_event(duration, description, date, price):           #figure it out how to add the location and the event type
    """Creat and return an event"""

    event = Event(duration=duration,
                description=description, 
                date=date, price=price)

    return event


def get_event_by_id(id):                                               #getting events from database
    """Return all events."""

    return Event.query.get(id)    





def create_event_type(name):
    """Create and return an event type"""

    event_type = Event_type(name=name)    

    return event_type

def get_event_type():
    """Return all events title"""

   
    return Event_type.query.all()







def create_location(venue_name, address, city, state, zipcode): 
    """Create and return a location"""

    location = Location(venue_name=venue_name,
                        address=address, city=city,
                        state=state, 
                        zipcode=zipcode )

    return location

def get_location(id):
    """Return all locations"""

    return Location.query.get(id)


    # figure out about attendance table












if __name__ == '__main__':
    from server import app
    connect_to_db(app, "tango-project")