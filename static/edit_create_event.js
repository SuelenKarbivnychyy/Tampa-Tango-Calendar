let cancelButton = document.getElementById("cancel");

const CancelAddNewEvent = (evt) => {
    evt.preventDefault();
}    

cancelButton.addEventListener("click", CancelAddNewEvent);