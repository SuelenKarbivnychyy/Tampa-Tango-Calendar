



Welcome to Tampa Tango Calendar, the one-stop place to know about all tango-related events happening in the area. 
You can register to events, syncronize plans with your social network accounts and calendar, put reviews, get emails and much more! 
  
  

## Contents

* [Tech Stack](#tech-stack)

* [Features](#features)

* [Installation](#install)

  

## <a name="tech-stack"></a>Tech Stack

* Python
* Javascript 
* Flask
* Jinja2
* PostgreSQL
* SQLAlchemy ORM
* Bootstrap
* SengGrid API


  

## <a name="features"></a>Features

  
  

#### Events Page

On this page user can see all the events happening in the area in calendar order. Every event will have description, date, average rating. Buttons on the bottom of event card can help register for the event, cancel registration, share even on a Facebook profile and add it to the Google Calendar.
    

#### Profile Page

User Profile is the page where the user can see all the event he signed in for, and manage that list. Also the user can see all reviews he created for the events and delete them if we want so.
  

#### Event Details Page

To get to the Event Details page user can click on any event card in the "Events" page or "Profile" page. 
Information on event details will show where the event is happening, what is the date, time and cost of the event, how many people are registered for the event aleady.
Also user can add or edit his review for particular event and read what other say. 

  

#### Registration Page

Users who are not logged in will see "Create Account" link in the navigation bar. User has to provide first and last name and unique email plus password to register. Then email and password should be used to log in to the system which will allow to register for the emails and recieve email updates. 

  
#### Administrator Page

This page has limited access - you have to be registered as system administrator to see it in the navigation bar. The intend of this page to work with list of the events by adding new ones, deleting events, adding new types of events and locations where events can happen.
Also for this page Administrator can send email updates to all registered users. 

#### Add New Event Page
This page has limited access - you have to be registered as system administrator to have access to this page. It shows when the admin user adding event and provides set of fields to be filled with information.  

## <a name="install"></a>Installation

To run Tampa Tango Calendar on your machine:

  

1) Install PostgreSQL

  

Clone or fork this repo:

```
https://github.com/SuelenKarbivnychyy/Final-Project
```

  

Create and activate a virtual environment inside your Tampa Tango Caledar directory:

```
virtualenv env
source env/bin/activate
```

  

Install the dependencies:

```
pip install -r requirements.txt
```

  

Sign up to use the [SendGrid API](https://sendgrid.com/)

Create secrets.sh and put 
```
export EMAIL_KEY="secret goes here"
```

  

Set up the database:

  

```
python3 seed_database.py
```

  

Run the app:

  

```
python3 server.py
```

  

You can now navigate to 'localhost:5000/' to access Tampa Tango Calendar.