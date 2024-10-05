function vladi(array) {
  let turnQty = Number(array[0]);
  let result = 0;
  let toTen = 0;
  let toTwenty = 0;
  let toThirty = 0;
  let toForty = 0;
  let toFifty = 0;
  let invalid = 0;

  for (let turn = 1; turn <= turnQty; turn++) {
    currentTurn = array[turn];

    if (currentTurn < 0 || currentTurn > 50) {
      invalid += 1;
      result /= 2;
      continue;
    } else if (currentTurn >= 0 && currentTurn <= 9) {
      result += currentTurn * 0.2;
      toTen += 1;
    } else if (currentTurn >= 10 && currentTurn <= 19) {
      result += currentTurn * 0.3;
      toTwenty += 1;
    } else if (currentTurn >= 20 && currentTurn <= 29) {
      result += currentTurn * 0.4;
      toThirty += 1;
    } else if (currentTurn >= 30 && currentTurn <= 39) {
      result += 50;
      toForty += 1;
    } else if (currentTurn >= 40 && currentTurn <= 50) {
      result += 100;
      toFifty += 1;
    }
  }

  console.log(result.toFixed(2));
  console.log(`From 0 to 9: ${((100 * toTen) / turnQty).toFixed(2)}%`);
  console.log(`From 10 to 19: ${((100 * toTwenty) / turnQty).toFixed(2)}%`);
  console.log(`From 20 to 29: ${((100 * toThirty) / turnQty).toFixed(2)}%`);
  console.log(`From 30 to 39: ${((100 * toForty) / turnQty).toFixed(2)}%`);
  console.log(`From 40 to 50: ${((100 * toFifty) / turnQty).toFixed(2)}%`);
  console.log(`Invalid numbers: ${((100 * invalid) / turnQty).toFixed(2)}%`);
}

vladi(["10", "43", "57", "-12", "23", "12", "0", "50", "40", "30", "20"]);
