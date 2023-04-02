let createAccountButton = document.getElementById("create_account");

const validateUserEmail = (evt) => {    
    evt.preventDefault();
    
    let fNameInput = document.getElementById("firstname-input").value;
    let lNameInput = document.getElementById("lastname-input").value;
    let passwordInput = document.getElementById("password-input").value;
    let emailInput = document.getElementById("email-input").value;
    // console.log(fNameInput, lNameInput, passwordInput, emailInput);

    if (fNameInput === '' || lNameInput === '' || passwordInput === '' || emailInput === '') {                   // checking if all the fields are filled and let the user now if its not
        display_warning_message("All fields are required", "Please check your informations and try again")
        return ;     
    } else if (! emailInput.includes("@") || ! emailInput.includes(".com")) {
        display_warning_message("Invalid email", "Make sure you entered a valid email contaning'@' and '.com' at it.")
        return ;
    }   

    let emailInputValue = document.getElementById("email-input").value;                     // alert(emailInputValue);

    const emailValidation = {                                                               //object. the keys are the expected value from server.py and value is the value from browser
        email: emailInputValue          
    }

    fetch('/check_email_exist', {
        method: 'POST',
        body: JSON.stringify(emailValidation),               // body takes in a object
        headers: {
            'Content-Type': 'application/json',
        },
    })  
        .then((response) => response.text())
        .then(createAccount);                                   // .then function is taking the routeUser function as parameter 
} 

const redirectHandler = () => {
    document.getElementById("submit_form").submit();
}

const createAccount = (data) => {                               // the response from server as "data"
    
    if (data == "true") {                                   //checking what the response from server will be
        display_warning_message("It looks like you already have an account", "Please login");
    }
    else {
        display_warning_message("Successfully created an account", "You are welcome", redirectHandler);                  
    }
}

createAccountButton.addEventListener('click', validateUserEmail);




