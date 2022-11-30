submitReviewButton = document.getElementById("review_button");

const submitReview = (evt) => {
    evt.preventDefault();

    let rate = document.getElementById("rate_id").value;
    let review = document.getElementById("review_text").value;
    let eventId = document.getElementById("event_id").innerHTML;
    

    const createRateAndReview = {                                  //object. the keys are the expected value from server.py and value is the value from browser
        user_rate: rate, 
        user_review: review,  
        event_id: eventId
    }
    alert(rate);
    alert(review);

    fetch('/review', {
        method: 'POST',
        body: JSON.stringify(createRateAndReview),                      // body takes in a object
        headers: {
            'Content-Type': 'application/json',
        },
    })  
        .then((response) => response.text())
        .then(userResponse); 

}

const userResponse = (data) => {
    if (data == "true") {
        alert("review sucessfully added");
    }
    else if (data == "false") {
        alert("you've reviewd this event already");
    }
}



submitReviewButton.addEventListener('click', submitReview);