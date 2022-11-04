let button = document.getElementById("submit");

const getEmail = () => {
    let getEmail = document.getElementById("password").value;
    print(getEmail);
} 

button.addEventListener('click', getEmail);
