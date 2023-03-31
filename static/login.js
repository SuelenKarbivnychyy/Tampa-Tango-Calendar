let button = document.getElementById("submit");

const validateUserCredentials = (evt) => {
    evt.preventDefault();

    let emailImputValue = document.getElementById("email").value;
    let passwordImputValue = document.getElementById("password").value;
    
    if (emailImputValue === '' || passwordImputValue === '') {         // checking if all the fields are filled and let the users now if its not
        display_warning_message("All the fields are required", "Please verify the informations and try again");   
        return ;    
    } 
    
    const emailValidation = {                                  //object. the keys are the expected value from server.py and value is the value from browser
        email: emailImputValue, 
        password: passwordImputValue       
    }

    fetch('/validate_user_credentials', {
        method: 'POST',
        body: JSON.stringify(emailValidation),                      // body takes in a object
        headers: {
            'Content-Type': 'application/json',
        },
    })  
        .then((response) => response.text())
        .then(routeUser);                                       // .then function is taking the routeUser function as parameter 
} 

function redirectToCreateAccount() {
    window.location.href = "/create_account"; 
}



const routeUser = (data) => {                                 // the response from server as "data"
    // alert(data);

    if (data == "true") {                                   //checking what the response from server will be
        window.location.href = "/events";                  // redirecting to that route if condition is true
    } else if (data == "no result") {
        display_warning_message("Please create an account", "No registers for this email in the records.", redirectToCreateAccount);                               //taking a call back function as second parameter
    } else {
        window.location.href = "/" ;       
    }
}

if (button) {
    button.addEventListener('click', validateUserCredentials);
}

