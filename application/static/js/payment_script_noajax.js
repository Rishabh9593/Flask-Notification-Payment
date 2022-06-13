var stripe = Stripe(checkout_public_key);

const button = document.querySelector('#pay_now_btn');

button.addEventListener('click',event => {
    stripe.redirectToCheckout({
        sessionId: checkout_session_id,
  
    }).then(function(result){

    });
})