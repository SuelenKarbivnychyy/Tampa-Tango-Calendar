let signInButton = document.querySelectorAll('[name="sign_up"]');

const signInForEvent = (evt) => {
    evt.preventDefault();

    let button = evt.target;
    let eventId = button.value;
    // alert(eventId);
    

    const countAttendance = {
        event_id : eventId        
    }

    fetch('/event_attendance', {
        method: 'POST',
        body: JSON.stringify(countAttendance),
        headers: {
            'Content-Type': 'application/json',
        },
    })  
        .then((response) => response.text())
        .then(serverData)        
}

const serverData = (data) => {
    alert(data);

    window.location.href = "/events";

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
    alert(data);
    window.location.href = "/events";

}

for (button of signOutButton) {                                                          // adding event handler for each button
    button.addEventListener('click', signOutFromEvent);
};

