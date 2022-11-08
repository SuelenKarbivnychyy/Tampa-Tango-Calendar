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


// createAccount = document.getElementById("create_account");

// const createAccountUser = () => {
//     let inputFname = document.getElementById("firstname-input").value;
//     let inputLname = document.getElementById("lastname-input").value;
//     let inputEmail = document.getElementById("email-input").value;
//     let inputPassword = document.getElementById("password-input").value;
// }

// createAccount.addEventListener('click', createAccountUser);