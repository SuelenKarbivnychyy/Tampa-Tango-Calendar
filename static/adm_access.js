subscribe_button = document.getElementById("subscribe");

const sendEmail = (evt) => {
    evt.preventDefault();

fetch("/send_email", {
    method: 'POST',  
    headers: {
        'Content-Type': 'application/json',
    },
})  
    .then((response) => response.text())
    .then(serverAnswer);    

}

const serverAnswer = (data) => {

    if (data == "true") {
        display_warning_message("Sent", "Your email were successfully sent.");
    } else {
        display_warning_message("Error", "Please try again.");
    }
}

// window.location.href = "/adm";

subscribe_button.addEventListener('click', sendEmail);




let addNewVenue = document.getElementById("add_event_location");

const performValidation = (evt) => {    

    let venueName = document.getElementById("venue_name").value;
    let venueStreet = document.getElementById("address_input").value;
    let venueCity = document.getElementById("city_input").value;
    let venueState = document.getElementById("state_input").value;
    let venueZipcode = document.getElementById("zipcode_input").value;

    if (venueName === '' || venueStreet === '' || venueCity === '' || venueState === '' || venueZipcode === '') {
        display_warning_message("All the fields are required", "Please verify the informations and try again.");   
        evt.preventDefault();
    } 
}    
addNewVenue.addEventListener("click", performValidation);