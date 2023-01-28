"""CRUD operations."""

from model import db, Event, Event_type, Location, User, Attendance, Review, connect_to_db



def create_user(fname, lname, email, password, is_adm=False):
    """Create and return a new user."""

    user = User(fname=fname,
                lname=lname,
                email=email,
                password=password,
                is_adm=is_adm)

    return user


def get_user_by_email(email):                       #return a user with that email if exists, return none otherwise
    """Return a user by email."""    

    return User.query.filter(User.email == email).first()  

def get_user_by_id(id):
    """Return an user by id"""

    return User.query.filter(User.id == id).first()

def get_all_users():
    """Return all users"""   

    return User.query.all()


    
def create_review(rate, comment, event_id, user_id):
    """Create an return a review"""

    review = Review(rate=rate, comment=comment, event_id=event_id, user_id=user_id)
    return review


def get_all_reviews_for_a_user(user_id):
    """Return all reviews"""

    return Review.query.filter(Review.user_id == user_id).all()


def get_review_by_event_and_user(event_id, user_id):
    """Return review by event id and user_id"""

    return Review.query.filter(Review.event_id == event_id, Review.user_id == user_id).first()


def get_review_by_id(review_id):
    """Return a review by id"""

    return Review.query.filter(Review.id == review_id).first() 


def get_all_reviews_by_event_id(event_id):
    """Return all the reviews for an event"""

    return Review.query.filter(Review.event_id == event_id).all()   



def create_event(name, description, start_date_time, end_date_time, price, location_id, event_type_id):           #figure it out how to add the location and the event type
    """Creat and return an event"""

    event = Event(name=name,
                
                description=description, 
                start_date_time=start_date_time,
                end_date_time=end_date_time,
                price=price,
                location_id=location_id,
                event_type_id=event_type_id)

    return event


def get_event_by_id(id):                                               
    """Return events by id"""

    return Event.query.get(id)  


def get_all_events():                                               
    """Return all events"""
    
    return Event.query.order_by('start_date_time').all()
   


def get_event_id_and_name():

    return db.session.query(Event_type.id, Event_type.name).all()


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




def create_attendance(event_id, user_id):
    """Create and return a attendance"""

    attendance = Attendance(event_id=event_id,
                            user_id=user_id)

    return attendance  



def delete_attendance(id, event_id, user_id):
    """Delete a attendance"""   

    delete = Attendance(id=id, event_id=event_id, user_id=user_id)      

    return delete               



def get_attendance(event_id, user_id):
    """Return an attendance"""

    return Attendance.query.filter(Attendance.event_id == event_id, Attendance.user_id == user_id).first()



def get_all_attendance():
    """Return all attendances"""
   
    return db.session.query(Attendance.event_id, db.func.count(Attendance.id)).join(Event, Attendance.event_id == Event.id).join(Event_type, Event.event_type_id == Event_type.id).group_by(Attendance.event_id).all()



def get_all_attendance_for_a_user(user_id):

    return Attendance.query.filter(Attendance.user_id == user_id).all()                 #returning a list of attendance objects













if __name__ == '__main__':
    from server import app
    connect_to_db(app, "tango-project")