let button = document.getElementById("submit");

const validateUserCredentials = (evt) => {
    evt.preventDefault();
    let emailImputValue = document.getElementById("email").value;
    let passwordImputValue = document.getElementById("password").value;
    // alert(emailImputValue);
    
    const emailValidation = {                                  //object. the keys are the expected value from server.py and value is the value from browser
        email: emailImputValue, 
        password: passwordImputValue       
    }

    fetch('/check_email', {
        method: 'POST',
        body: JSON.stringify(emailValidation),                  // body takes in a object
        headers: {
            'Content-Type': 'application/json',
        },
    })  
        .then((response) => response.text())
        .then(routeUser);                                   // .then function is taking the routeUser function as parameter 
} 

const routeUser = (data) => {                               // the response from server as "data"
    alert(data);

    if (data == "welcome") {                                //checking what the response from server will be
        window.location.href = "/events";                  // redirecting to that route if condition is true
    }
    else if (data == "no result") {
        window.location.href = "/create_account";
    }
    else {
        window.location.href = "/" ;       
    }
}

button.addEventListener('click', validateUserCredentials);






// create the logic for check if email already in data base for creating an account


let createAccountButton = document.getElementById("create_account");

const validateUserEmail = (evt) => {
    evt.preventDefault();
    let emailImputValue = document.getElementById("email-input").value;
    
    // alert(emailImputValue);
    
    const emailValidation = {                                  //object. the keys are the expected value from server.py and value is the value from browser
        email: emailImputValue          
    }

    fetch('/create_account', {
        method: 'POST',
        body: JSON.stringify(emailValidation),                  // body takes in a object
        headers: {
            'Content-Type': 'application/json',
        },
    })  
        .then((response) => response.text())
        .then(emailUser);                                   // .then function is taking the routeUser function as parameter 
} 

const emailUser = (data) => {                               // the response from server as "data"
    alert(data);

    if (data == "You already have an account") {                                //checking what the response from server will be
        window.location.href = "/events";                  // redirecting to that route if condition is true
    }
    else if (data == "Sucessfully created an account. Welcome") {
        window.location.href = "/";
    }
    else {
        window.location.href = "/" ;       
    }
}

createAccountButton.addEventListener('click', validateUserEmail);








// implement a flash message to the adm on delete event. "are you sure you want to delete this event?"