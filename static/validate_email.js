

let createAccountButton = document.getElementById("create_account");

const validateUserEmail = (evt) => {    
    evt.preventDefault();
    let emailImputValue = document.getElementById("email-input").value;    
    // alert(emailImputValue);
    
    const emailValidation = {                                  //object. the keys are the expected value from server.py and value is the value from browser
        email: emailImputValue          
    }

    fetch('/validate_email', {
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
    // alert(data);

    if (data == "true") {                                //checking what the response from server will be
        alert("Already existe an account with this email");
    }
    else {
        alert("Sucessfully created an account")
        document.getElementById("submit_form").submit();
          
    }
}
createAccountButton.addEventListener('click', validateUserEmail);