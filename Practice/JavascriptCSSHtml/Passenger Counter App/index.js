       
let peopleCount = document.getElementById("people-el");
let entryCount = document.getElementById("entry-el");
var entries = 0;

function increment() {
    peopleCount.innerText = Number(peopleCount.innerText) + 1;
}

function reduce() {
    if (peopleCount.innerText > 0) {
        peopleCount.innerText = Number(peopleCount.innerText) - 1;
    } 
}

function save() {
    if (Number(peopleCount.innerText) != 0)
        if (entries > 0) {
            entryCount.innerText += " - " + peopleCount.innerText;
        } else {
            entryCount.innerText += " " + peopleCount.innerText;
            entries += 1;
        }
        peopleCount.innerText = "0"
}