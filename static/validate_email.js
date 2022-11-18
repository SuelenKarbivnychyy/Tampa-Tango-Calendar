let createAccountButton = document.getElementById("create_account");

const validateUserEmail = (evt) => {    
    evt.preventDefault();
    
    let fNameInput = document.getElementById("firstname-input").value;
    let lNameInput = document.getElementById("lastname-input").value;
    let passwordInput = document.getElementById("password-input").value;
    let emailInput = document.getElementById("email-input").value;
    // console.log(fNameInput, lNameInput, passwordInput, emailInput);

    if (fNameInput === '' || lNameInput === '' || passwordInput === '' || emailInput === '') {                   // checking if all the fields are filled and let the user now if its not
        display_warning_message("All fields are required")
        return ;     
    }    

    let emailImputValue = document.getElementById("email-input").value;                     // alert(emailImputValue);

    const emailValidation = {                                                               //object. the keys are the expected value from server.py and value is the value from browser
        email: emailImputValue          
    }

    fetch('/validate_email', {
        method: 'POST',
        body: JSON.stringify(emailValidation),               // body takes in a object
        headers: {
            'Content-Type': 'application/json',
        },
    })  
        .then((response) => response.text())
        .then(emailUser);                                   // .then function is taking the routeUser function as parameter 
} 

const redirectHandler = () => {
    document.getElementById("submit_form").submit();
}

const emailUser = (data) => {                               // the response from server as "data"
    
    if (data == "true") {                                   //checking what the response from server will be
        display_warning_message("You already have an account please login");
    }
    else {
        display_warning_message("Sucessfully created an account", redirectHandler);                  
    }
}

createAccountButton.addEventListener('click', validateUserEmail);




