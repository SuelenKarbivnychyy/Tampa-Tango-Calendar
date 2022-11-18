let signInButton = document.querySelectorAll('[name="sign_up"]');

const signInForEvent = (evt) => {
    evt.preventDefault();

    let button = evt.target;
    let eventId = button.value;    

    const countAttendance = {
        event_id : eventId        
    }

    fetch('/event_sign_in', {
        method: 'POST',
        body: JSON.stringify(countAttendance),
        headers: {
            'Content-Type': 'application/json',
        },
    })  
        .then((response) => response.text())
        .then(serverData)        
}

const redirect_after_action = () => {
    window.location.href = "/events";
}

const serverData = (data) => {
    display_warning_message("You're sucessfully sign in for this event.", redirect_after_action)
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
    display_warning_message("You are sign out.", redirect_after_action);    
}

for (button of signOutButton) {                                                          // adding event handler for each button
    button.addEventListener('click', signOutFromEvent);
};

