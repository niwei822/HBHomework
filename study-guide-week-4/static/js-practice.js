'use strict';

/** ********************
 Make an Event Handler
********************* */

// Your Code Here
const button = document.querySelector('#popup-alert-button');
button.addEventListener('click', () => alert('Hello!'));
/** ***********************
Practice Your Times Tables
************************ */

// Your Code Here
const multiplyForm = document.querySelector('#multiplying-form');
multiplyForm.addEventListener('submit', (evt) => {
  evt.preventDefault();

  const multiplesOf = Number(document.querySelector('#mults-of').value);
  const max = Number(document.querySelector('#max').value);
  const multiples = [];
  let nextMultiple = multiplesOf;

  while (nextMultiple <= max) {
    multiples.push(nextMultiple);
    nextMultiple += multiplesOf;
  }

  console.log(multiples);
});
/** **************
An Agreeable Form
*************** */

// Your Code Here
document.querySelector('#agreeable-form').addEventListener('submit', (event) => {
  event.preventDefault();
  const favoriteFood = document.querySelector('#favorite-food-input').value;
  document.querySelector('#agreeable-text').textContent = `I like ${favoriteFood}, too!`;
});
/** ****************
Five colored primes
***************** */

const PRIME_COLORS = ['orange', 'midnightblue', 'darkgoldenrod', 'green', 'purple'];

// Your Code Here
function isPrime(x) {
  // is X prime?

  for (let i = 2; i * i <= x; i++) {
    if (x % i === 0) {
      return false;
    }
  }
  // We never found a divisor, so it's prime
  return true;
}

function makePrimes() {
  let num = 2; // find primes higher than 1
  let numFound = 0;
  document.querySelector('#prime-circle-area').innerHTML = '';
  while (numFound < 5) {
    if (isPrime(num)) {
      const circleArea = document.querySelector('#prime-circle-area');
      circleArea.insertAdjacentHTML(
        'beforeend',
        `<div class="prime-circle" style="background-color:${PRIME_COLORS[numFound]}">${num}</div>`,
      );
      numFound += 1;
    }
    num += 1;
  }
}
document.querySelector('#make-prime-circles').addEventListener('click', makePrimes);
/** *********
Got Puppies?
********** */

// NOTE: DO NOT CHANGE THE CODE OF THIS FUNCTION
function showPuppies(results) {
  // get the URL for the puppy photo out of the results object
  const puppyURL = results.url;
  const puppyDiv = document.querySelector('#puppies-go-here');
  // clear anything currently in the div
  puppyDiv.innerHTML = null;
  // add the img element
  puppyDiv.insertAdjacentHTML('beforeend', `<img src=${puppyURL} alt="puppy-image">`);
}

// Your Code Here
document.querySelector('#puppy-form').addEventListener('submit', (event) => {
  // prevent the form from triggering a page load
  event.preventDefault();

  // get the number of puppies selected from the input
  const numPuppies = document.querySelector('#num-puppies').value;
  // make the AJAX request
  // GET requests cannot have a body so we use a query string
  fetch(`/puppies.json?num-puppies=${numPuppies}`)
    .then((response) => response.json())
    .then((jsonResponse) => {
      showPuppies(jsonResponse);
    });
});