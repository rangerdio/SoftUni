function vladi(input) {
  let ages = Number(input[0]);
  let washMPrice = Number(input[1]);
  let toyPrice = Number(input[2]);
  let sumMoneyPresents = 0;
  let toyMoneyPresents = 0;
  let moneyPresentAmount = 0;
  let diff = 0;

  for (let age = 1; age <= ages; age++) {
    if (age % 2 === 0) {
      moneyPresentAmount += 10;
      sumMoneyPresents += moneyPresentAmount - 1;
    } else {
      toyMoneyPresents += toyPrice;
    }
  }

  diff = (Math.abs(washMPrice - (toyMoneyPresents + sumMoneyPresents))).toFixed(2);
  if (washMPrice <= toyMoneyPresents + sumMoneyPresents) {
    console.log(`Yes! ${diff}`);
  } else {
    console.log(`No! ${diff}`);
  }
}

vladi(["10", "170.00", "6"]);
vladi(["21", "1570.98", "3"]);
