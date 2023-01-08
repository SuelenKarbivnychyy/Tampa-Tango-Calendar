



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

In the Marketplace, user can see all games being sold and filter to see only ones matching their wishlist or listings for recommended games. To recommend games, the app's algorithm analyzes the games the user owns or wishes to own, finds the top three mechanics and categories for a total of 6 traits, and finds matches in the marketplace that have at least one of these traits, not including any games the user already owns or wishes to own. The matched traits are shown along with the results.

  


#### Administrator Page

To learn more about a game listing, user can click on the game name. A modal appears with the listing comment, if any, along with standard game details. If the seller has any other games listed in the Marketplace, a button will appear for the user to filter all the marketplace listings by that seller. If user is interested in contacting the seller, they can click on the button to open up a new email in their default email client, with the seller email address in the TO field and the game name in the email subject prepopulated.

  

## <a name="install"></a>Installation

To run Tampa Tango Calendar on your machine:

  

1) Install PostgreSQL

  

Clone or fork this repo:

```

https://github.com/SuelenKarbivnychyy/Final-Project

```

  

Create and activate a virtual environment inside your Board Game Village directory:

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