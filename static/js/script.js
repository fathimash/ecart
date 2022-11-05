//................ #checkout..........................................


let inc = 0;
var names = ["Maurice Lacroix", "Rider", "U-Boat"];
var prices = ["575.99", "59.99", "7550.99"];

const items = document.querySelectorAll(".items");
const clear = document.querySelectorAll(".clear");
const main = document.querySelectorAll(".main");
const wrap = document.querySelector("#wrapper");

const list0 = document.querySelector("#items-list0");
const list1 = document.querySelector("#items-list1");
const list2 = document.querySelector("#items-list2");
const total = document.querySelector("#total");
const checkprice = document.querySelector("#checkprice");

items[0].addEventListener("change", (event) => {
  list0.innerHTML =
    names[0] + "<br>" + "&pound;" + prices[0] * event.currentTarget.value;
  var total1 =
    prices[0] * items[0].value +
    prices[1] * items[1].value +
    prices[2] * items[2].value;
  total.innerHTML = total1.toFixed(2);
});
items[1].addEventListener("change", (event) => {
  list1.innerHTML =
    names[1] + "<br>" + "&pound;" + prices[1] * event.currentTarget.value;
  total2 =
    prices[0] * items[0].value +
    prices[1] * items[1].value +
    prices[2] * items[2].value;
  total.innerHTML = total2.toFixed(2);
});
items[2].addEventListener("change", (event) => {
  list2.innerHTML =
    names[2] + "<br>" + "&pound;" + prices[2] * event.currentTarget.value;
  total3 =
    prices[0] * items[0].value +
    prices[1] * items[1].value +
    prices[2] * items[2].value;
  total.innerHTML = total3.toFixed(2);
});
clear[0].addEventListener("click", function () {
  for (var i = 0; i < 3; i++) {
    items[i].value = 0;
  }
  list0.innerHTML = "";
  list1.innerHTML = "";
  list2.innerHTML = "";
  total.innerHTML = "";
});
checkout.addEventListener("click", function () {
  wrapper.style.display = "none";
  main[0].style.display = "block";
  if (total.innerHTML == "") {
    total.innerHTML = "0";
    checkprice.innerHTML = "Checkout Value = &pound;" + total.innerHTML;
  } else {
    checkprice.innerHTML = "Checkout Value = &pound;" + total.innerHTML;
  }
});
returning.addEventListener("click", function () {
  wrapper.style.display = "block";
  main[0].style.display = "none";
});


