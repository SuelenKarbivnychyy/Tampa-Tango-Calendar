let signInButton = document.querySelectorAll("button");

const signInForEvent = (evt) => {
    evt.preventDefault();

    let button = evt.target;
    let eventId = button.value;
    alert(eventId);
    

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
        .then(serverAnswer)        
}

const serverAnswer = (data) => {
    alert(data);
}






for (button of signInButton) {                                                          // adding event handler for each button
   button.addEventListener('click', signInForEvent);
};



