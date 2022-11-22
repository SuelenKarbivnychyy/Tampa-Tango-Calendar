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
        display_warning_message("Sent", "Your email were sucessfully send.");
    } else {
        display_warning_message("Error", "Please try again.");
    }
}

// window.location.href = "/adm";

subscribe_button.addEventListener('click', sendEmail);