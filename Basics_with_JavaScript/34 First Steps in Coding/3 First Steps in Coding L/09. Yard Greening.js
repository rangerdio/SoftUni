function asd(input) {;

let area = Number(input[0]);
let sqMeterPrice = 7.61;
let discount = 18;

moneyToPay = sqMeterPrice * area;
discount = moneyToPay * (18 / 100) ;
console.log(`The final price is: ${moneyToPay - discount} lv.`);
console.log(`The discount is: ${discount} lv.`);

};

asd(["150"]);
