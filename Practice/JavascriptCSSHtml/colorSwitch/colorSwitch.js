

function changeColor() {
    let colors = ['red', 'white', 'blue', 'green', 'pink', 'black', 'gray', 'yellow', 'orange'];
    let randomColor = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.backgroundColor = randomColor;
}
 
