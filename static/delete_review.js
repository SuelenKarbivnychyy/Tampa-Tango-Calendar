let deleteReviewButton = document.querySelectorAll('[name="delete_review"]');

const deleteReview = (evt) => {
    evt.preventDefault();

    let buttonDelete = evt.target;
    let reviewId = buttonDelete.value;

    const checkReview = {
        review_id : reviewId
    }

    fetch("/delete_review", {
        method: 'POST',
        body: JSON.stringify(checkReview),
        headers: {
            'Content-Type' : 'application/json',
        },
    })

        .then((response) => response.text())
        .then(serverResponse)

}

function redirectToProfile() {
    window.location.href = "/user_profile"; 
}

const serverResponse = (data) => {
    
    if (data == "Review deleted") {
        display_warning_message("Review deleted", "Sucess deleted review", redirectToProfile);
    } else {
        display_warning_message("Review Already beeing deleted", "Thank you", redirectToProfile);
    }    

}

for (button of deleteReviewButton) {
    button.addEventListener('click', deleteReview);
};