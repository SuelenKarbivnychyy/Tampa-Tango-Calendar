//  THIS FILE IS FOR DISPLAY MESSAGES WARNING IN THE PAGES. THIS FILE WILL BE TAKEN AT BASE HTML. 

const display_warning_message = (message, callback = () => {}) => {

    const myModal = new bootstrap.Modal('#exampleModal', {                                                          //bootstrap function to show a wan=ening message instead of alert
        keyboard: false,

    })
    $("#exampleModal").on('hide.bs.modal', function (e) {
        callback.call();
    })
    document.getElementById("text").innerHTML = message;
    myModal.show()

}
