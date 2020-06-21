
var stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');


var elements = stripe.elements();

var style = {
  base: {
    
    fontSmoothing: 'antialiased',
    fontSize: '1em',
    '::placeholder': {

    }
     },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a'
  }
};

// Create an instance of the card Element.
var card = elements.create('card', {style: style});

// Add an instance of the card Element into the `card-element` <div>.
card.mount('#card-element');