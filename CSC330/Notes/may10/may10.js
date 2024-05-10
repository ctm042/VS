/*
The DOM aka the Document Object Model: Objects and methods already exist to access an html file. There is an object variable named document.
*/

// Declare a variable to hold a reference to the tag for the counter.
let counterElement = document.getElementById("counter");

// Test code to see that we can now manipulate the counter.
//counterElement.innerText = 99;

// Declare a variable to hold the counter value
let count = 0;

// Write a function that will increment count and change the html element.
function increment() {
    count++;
    counterElement.innerText = count;
}

// Write a function that named reset that will reset the counter element to 0  and initialize the count variable.
function reset() {
    count = 0
    counterElement.innerText = count;
}

// Write a function named save that will save the current count to the p tag by concatenating the text onto it.
let savedElement = document.getElementById("saved");
function save() {
    savedElement.innerText += (" " + count + ",");

}