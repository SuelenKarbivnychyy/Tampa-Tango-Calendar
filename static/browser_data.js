let button = document.getElementById("submit");

const validateUserCredentials = (evt) => {
    evt.preventDefault();

    let emailImputValue = document.getElementById("email").value;
    let passwordImputValue = document.getElementById("password").value;
    // alert(emailImputValue);
    if (emailImputValue === '' || passwordImputValue === '') {         // checking if all the fields are filled and let the users now if its not
        alert("All the fields are required");   
        return ;    
    } 
    
    
    const emailValidation = {                                  //object. the keys are the expected value from server.py and value is the value from browser
        email: emailImputValue, 
        password: passwordImputValue       
    }

    fetch('/validate_user_credentials', {
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

    if (data == "true") {                                //checking what the response from server will be
        window.location.href = "/events";                  // redirecting to that route if condition is true
    }
    else if (data == "false") {
        window.location.href = "/create_account";
    }
    else {
        window.location.href = "/" ;       
    }
}

button.addEventListener('click', validateUserCredentials);









// implement a flash message to the adm on delete event. "are you sure you want to delete this event?"