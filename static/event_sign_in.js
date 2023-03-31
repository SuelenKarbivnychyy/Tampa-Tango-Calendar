let signInButton = document.querySelectorAll('[name="sign_up"]');

const signInForEvent = (evt) => {
    evt.preventDefault();
    
    let button = evt.target;
    let eventId = button.value;    

    const eventData = {
        event_id : eventId        
    }

    fetch('/event_sign_in', {
        method: 'POST',
        body: JSON.stringify(eventData),
        headers: {
            'Content-Type': 'application/json',
        },
    })  
        .then((response) => response.text())
        .then(serverData)        
}

const redirect_after_action = () => {
    // window.location.href = "/events";
    window.location.href=window.location.href;
}

const serverData = (data) => {    
    if(data == "Please login.") {
        display_warning_message("Please login in.", "You need to login to register for a class.", redirect_after_action);
    } else {
        display_warning_message("Registered.", "You're sucessfully registered for this event.", redirect_after_action);
    }    
}

for (button of signInButton) {                                                          // adding event handler for each button
   button.addEventListener('click', signInForEvent);
};

// #################################################################################################################
// HANDLING THE SIGN OUT BUTTON

let signOutButton = document.querySelectorAll('[name="sign_out"]');

const signOutFromEvent = (evt) => {
    evt.preventDefault();  

    let button = evt.target;
    let eventId = button.value;  
    
    const checkAttendance = {
        event_id : eventId        
    }

    fetch('/sign_out', {
        method: 'POST',
        body: JSON.stringify(checkAttendance),
        headers: {
            'Content-Type': 'application/json',
        },
    })  
        .then((response) => response.text())
        .then(serverAnswer)        
}

const serverAnswer = (data) => {
    display_warning_message("You've sucessfully cancel your registration.", "We are sorry to see you go!", redirect_after_action);    
}

for (button of signOutButton) {                                                          // adding event handler for each button
    button.addEventListener('click', signOutFromEvent);
};


// adding event handler to the events in user_profile as well

let unGoButton = document.querySelectorAll('[name="un_going"]');

for (b of unGoButton) {
    b.addEventListener('click', signOutFromEvent);
};

