from flask import Flask, Blueprint, request, render_template, session, redirect
from model import connect_to_db, db
import crud


user_routing = Blueprint('user_routing', __name__, template_folder='templates')


@user_routing.route("/login", methods=["POST"])
def login():           
    """Check if user's credentials are correct to login"""    
   
    email_from_input = request.json.get("email")                                      #information from browser as json
    password = request.json.get("password")
    
    user_db = crud.get_user_by_email(email_from_input)                      #checking if the user's email input from the browser has any matchs at the database
    
    if user_db == None :                                                    #checking if user is not in db and return "no results if true"
        return "no result"  
   
    user_id= user_db.id
    user_password = user_db.password                                        #getting the password from db's user if there is a match
    if user_password == password:                                           #giving access to user if informations macth
        session['current_user'] = user_id
        session["user_name"] = f"{user_db.fname} {user_db.lname}"            #setting first name and last name from session
        is_administrator = user_db.is_adm
        session["is_adm"] = is_administrator        
        return "true"
    else:
        return "false"


@user_routing.route("/logout")
def logout():    
    """Logout user from session and redirect to homepage"""    

    session.pop('user_name')
    session.pop('current_user')
    session.pop('is_adm')
    return redirect('/')  


@user_routing.route("/create_account") 
def create_account():
    """Render create account template"""   

    return render_template("create_account.html") 


@user_routing.route("/check_email_exist", methods=["POST"])
def check_email_existl():
    """Validate email to create an account by check if the email is on database"""

    email = request.json.get("email")
    user = crud.get_user_by_email(email)
    if user != None:
        return "true"
    else:
        return "false"


@user_routing.route("/add_user_to_db", methods=["POST"])
def add_account():
    """Add an user account to database"""   

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    email = request.form.get("email")
    password = request.form.get("password") 

    new_user = crud.create_user(first_name, last_name, email, password)
    db.session.add(new_user)
    db.session.commit()     
    return redirect("/")  


@user_routing.route("/user_profile")
def display_user_profile():
    """Display user's profile"""
    
    user = session.get("current_user")    
    if user == None:
        return redirect('/')

    attendances = crud.get_all_attendance_for_a_user(user)
    events = []    
    for attendance in attendances:
        events.append(attendance.events)    

    user_reviews = crud.get_all_reviews_for_a_user(user)
    reviews = []
    for review in user_reviews:
        reviews.append(review) 
    return render_template("/user_profile.html", events=events, reviews=reviews)