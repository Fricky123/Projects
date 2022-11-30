// TEXTS
let cardsLabel = document.getElementById('cardsLabel-el');
let cards = document.getElementById('cards-el');
let sumText = document.getElementById('sum-el');
let declare = document.getElementById('declare-el');

// BUTTONS
let start = document.getElementById('start-el');
let draw = document.getElementById('draw-el');
let chooseOne = document.getElementById('chooseOne-el');
let chooseEleven = document.getElementById('chooseEleven-el');

// VARIABLES
var card = randomNumber();
var sum = 0;
var listOfCards = 0;
var cardCount = 0;

// MAIN FUNCTIONS
function startGame() {
    sum = 0;
    listOfCards = 0;
    start.innerText = "NEW GAME";
    cards.innerText = "Cards: ";
    sumText.innerText = 'Sum: ';
    declare.innerText = "";

    // start.style.visibility = "hidden";
    draw.style.visibility = "visible";    
}

function drawCards() {
    // start.style.visibility = "hidden";
    card = randomNumber();
    card2 = randomNumber();
    sum += card;

    if (cardCount == 0) {
        cards.innerText += ' ' + card + ' - ' + card2;
        cardCount += 1;
        
        if (card == 'ace' || card2 =='ace'){
            sum = ' ';
        } else {
            sum += card2;
        }
    } else {
        cards.innerText += " - " + card;
    }


    sumText.innerText = "Sum: " + sum;
    checkResult();
}

function checkResult() {
    if (sum > 21) {
        declare.innerText = "You lost";
        start.style.visibility = "visible";
        draw.style.visibility = "hidden"; 
        cardCount = 0;
    } 
    else if (sum === 21) {
        declare.innerText = "You WON!";
        start.style.visibility = "visible";
        draw.style.visibility = "hidden"; 
        cardCount = 0;
    }
    
}


// UTILITY FUNCTIONS
function randomNumber() { 
    i = Math.floor(Math.random() * (13 - 1 + 1) + 1);
    if (i == 1) {
        if (sum + 10 > 21) {
            return 1;
        } else {
            return 10;
        }
    } else if (i > 10) {
        return 10;
    } else {
        return i;
    }
} 

// START SEQUENCE
draw.style.visibility = "hidden"; 




