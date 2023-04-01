from flask import Flask, Blueprint, request, render_template, session
from model import connect_to_db, db
import crud


event_routing = Blueprint('event_routing', __name__, template_folder='templates')


@event_routing.route("/events")
def show_all_events(): 
    """View all events"""

    events = crud.get_all_events()
    rate = {}  

    for event in events:
        total_review_rate = 0
        for review in event.reviews:
            total_review_rate += review.rate
        total_reviews_per_event = len(event.reviews)
        rate_character = "⭐"
        if total_review_rate > 0:
            average_rate_per_event = round(total_review_rate / total_reviews_per_event)
            rate[event.id] = rate_character * average_rate_per_event
    
    list_of_attendance = crud.get_all_attendance()
    user_id = session.get("current_user")    
    current_user_events={}

    if user_id != None:    
        attendances = crud.get_all_attendance_for_a_user(user_id)  
        for attendance in attendances:
            current_user_events[attendance.event_id] = "true"    
    return render_template("events.html", events=events,
                                        attendances=current_user_events,
                                        attendance_number = list_of_attendance,
                                        rate=rate
                                        )


@event_routing.route("/events/<id>")    
def show_event_details(id):
    """View event details"""

    user = session.get("current_user")
    event = crud.get_event_by_id(id)
    review = crud.get_review_by_event_and_user(event.id, user)
    reviews_db = crud.get_all_reviews_by_event_id(event.id)    
    return render_template("events_details.html", event = event, review = review, reviews_db = reviews_db)


@event_routing.route("/event_sign_in", methods=["POST"])
def sign_in_for_event():
    """Register user to attend an event"""    

    event_id = request.json.get("event_id")
    user_id = session.get('current_user')
    if user_id == None:                                                                                  #if user not in session it will not allows user to sign in for event
        return "Please login."

    check_attendance = crud.get_attendance(event_id, user_id)        
    if check_attendance == None:   
        add_attendance = crud.create_attendance(event_id, user_id)
        db.session.add(add_attendance)        
        db.session.commit()        
        return "You are sucessfully sign in for this event."
    else:
        return "You are already sign in for this event."


@event_routing.route("/sign_out", methods=["POST"])    
def cancel_user_attendance():
    """Cancel user attendance to an event"""   

    event_id = request.json.get("event_id")
    user_id = session['current_user'] 
    attendance = crud.get_attendance(event_id, user_id)

    if attendance != None: 
        db.session.delete(attendance)
        db.session.commit()
        return "You are signed out for this event. We are sorry to let you go."
    else:
        return "You've signed out."      


@event_routing.route("/review", methods=["POST"])
def create_review():
    """Create a review"""

    event_id = request.json.get('event_id')
    user_id = session.get('current_user')    
    user_rate = request.json.get("user_rate")
    user_review = request.json.get("user_review")
    review_from_db = crud.get_review_by_event_and_user(event_id, user_id)
    
    if review_from_db == None:    
        new_review = crud.create_review(user_rate, user_review, event_id, user_id)
        db.session.add(new_review)
        db.session.commit()
        return "true"
    else:
        print(f"################## review {review_from_db.comment}")
        return "false"
    

@event_routing.route("/delete_review", methods=["POST"])
def delete_review():
    """Delete a review"""
    
    review_id = request.json.get('review_id')
    review_in_db = crud.get_review_by_id(review_id)    
    print(f"############################# review id: [{review_in_db}]")
    if review_in_db != None:
        db.session.delete(review_in_db)
        db.session.commit()
        return "Review deleted"
    else:
        return "deleted"    