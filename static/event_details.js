let listCards = document.querySelectorAll('[name="link_to_details"]');

 



const redirect_to_events_details = (evt) => {
    evt.preventDefault();

    let card = evt.target;
    if (card.className != "card-header") {
        card = card.parentElement;
    }
    let eventId = card.getAttribute('event_id');   
    
    let address = `/events/${eventId}`
    window.location.href = address;
    // alert(address)
}

for (card of listCards) {                                                          // adding event handler for each card
    card.addEventListener('click', redirect_to_events_details);
 };