const MAX_SCREEN_CONTENT = 16;

function setTheme(theme) {
    
}

const colorSelector = document.getElementById("color-selector");
colorSelector.addEventListener("change", (event) => {
    document.documentElement.className = event.currentTarget.value;
});


let calculationDone = false;

const calcScreenUpper = document.getElementById("calc-screen-upper");
const calcScreenLower = document.getElementById("calc-screen-lower");
const buttons = document.querySelectorAll(".symbol-button");
const valueButtons = document.querySelectorAll(".value-button");
const operationButtons = document.querySelectorAll(".operation-button");


valueButtons.forEach(element => {
    element.addEventListener("click", (event) => {
        if (calculationDone) {
            calcScreenUpper.innerHTML = "";
            calcScreenLower.innerHTML = "";
            calculationDone = !calculationDone;
        }
    })
});


operationButtons.forEach((element) => {
    element.addEventListener("click", (event) => {
        if (calculationDone) {
            calcScreenUpper.textContent = calcScreenLower.innerHTML;
            calculationDone = !calculationDone;

        }
    })
});


buttons.forEach(element => {
    element.addEventListener("click", (event)=>{
        
        if (calcScreenUpper.textContent.length < MAX_SCREEN_CONTENT) {
            calcScreenUpper.textContent += event.currentTarget.innerHTML;
        }
        else {
            alert("Max screen content reached.")
        }
    })   
});


const eqButton = document.getElementById("calc-button-eq");
eqButton.addEventListener("click", (event) => {
    let expression = calcScreenUpper.innerHTML;
    try {
        let result = math.evaluate(expression);
        calcScreenLower.innerHTML = math.format(result, {precision: 5}); //.toFixed(0);
        calculationDone = true;
    }
    catch {
        alert("Invalid expression")
        calcScreenUpper.innerHTML = "";
    }

});


const ceButton = document.getElementById("calc-button-CE");
ceButton.addEventListener("click", (event) => {
    calcScreenUpper.innerHTML = "";
    calcScreenLower.innerHTML = "";
});


const cButton = document.getElementById("calc-button-C");
cButton.addEventListener("click", (event) => {
    calcScreenUpper.innerHTML = calcScreenUpper.innerHTML.slice(0, calcScreenUpper.innerHTML.length-1);
    calcScreenLower.innerHTML = "";
    calculationDone = false;
});
