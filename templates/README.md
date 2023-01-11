



Welcome to Tampa Tango Calendar, the one-stop place to know about all tango-related events happening in Tampa area, state of Florida. 
Users are able to see all events available in the app, as well all proper information related to that event, the event's reviews, synchronize plans with your social network accounts and calendar. Users that have an active account are able to register for any event he is interesting at, review events he has attempt, and get emails updates.
  
  

## Contents

* [Tech Stack](#tech-stack)

* [Features](#features)

* [Installation](#install)

  

## <a name="tech-stack"></a>Tech Stack

* Python
* Javascript 
* Html
* Css
* Flask
* Jinja2
* PostgreSQL
* SQLAlchemy ORM
* Bootstrap
* SengGrid API


  

## <a name="features"></a>Features

  
  

#### Events Page

On this page, the user can see all the events available in the area in calendar order. Every event will display its description, date, time, and average rating. On the bottom of each event card, are implemented buttons to register for the event or cancel registration, share the event on his Facebook profile and add it to his Google Calendar. 



#### Profile Page

User Profile is the page where the user can see all the event he signed in for, and manage that list. Also, the user can see all reviews he created for the events and delete them if he wants so.
  

#### Event Details Page

To get to the Event Details page, the user can click on any event card in the "Events" page or "Profile" page. On this page are display Information about the event, such as price, how many people are going to this event, where the event is being held as well the address, and reviews available for this particular event. In this page, the user can leave a review for the event.

  

#### Registration Page

Users who are not logged in will see "Create Account" link in the navigation bar. User has to provide first and last name, value email plus password to register. Then email and password should be used to log in to the system which will allow him to receive email updates. 

  
#### Administrator Page

This page has limited access - you have to be registered as a system administrator to see it in the navigation bar. The intent of this page to work with the list of the events by adding new ones, deleting existent events, adding new types of events and venue locations where events may happen.
Also, on this page, Administrator are allowed to send email updates to all registered users. 

#### Add New Event Page
This page has limited access - you have to be registered as a system administrator to have access. This page is strict to the administrator to add new events or edit an existent event. There are a set of fields to be filled with details about the event.

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