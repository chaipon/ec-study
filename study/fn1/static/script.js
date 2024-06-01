const number = document.querySelector('#number');
const plusBtn = document.querySelector("#plus");
const minusBtn = document.querySelector("#minus");
const alertBtn = document.querySelector("#alert");
const logoutBtn = document.querySelector("#logout");
const colorBtn = document.querySelector("#color");
const targetEl = document.querySelector("div");

let count = 0;
let colorType = 0;

// console.log("hello");
plusBtn.onclick = function(event){
    count++;
    number.textContent = count;
};
minusBtn.onclick = function(event){
    count--;
    number.textContent = count;
};

alertBtn.onclick = function(event){
    window.alert("Count: " + count);
};
logoutBtn.onclick = function(event){
    console.log("Count:" + count);
};

colorBtn.onclick = function(event){

    console.log(colorType);
    switch(colorType){
        case 0:
            targetEl.style.background = "#ff0000";
            break;
        case 1:
            targetEl.style.background = "#0022ff";
            break;
        case 2:
            targetEl.style.background = "#00ff00";
            break;
        case 3:
            targetEl.style.background = "#ffffff";
            break;
        default:
            targetEl.style.background = "#ffffff";
            break;
    }
    colorType++;
    if(colorType > 3){
        colorType = 0;
    }
}