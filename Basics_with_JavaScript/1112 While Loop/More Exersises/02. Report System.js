function vladi(array) {
  let cashSum = 0;
  let cardSum = 0;
  let cashCount = 0;
  let cardCount = 0;
  let expectedIncome = Number(array[0]);
  let income = 0;
  let isMoneyGathered = false;

  let index = 0;
  index++;
  let command = array[index];

  while (command !== "End") {
    let currentItemPrice = Number(command);

    if (index % 2 !== 0 && currentItemPrice > 100) {
      console.log(`Error in transaction!`);
    } else if (index % 2 !== 0 && currentItemPrice <= 100) {
      income += currentItemPrice;
      cashSum += currentItemPrice;
      cashCount += 1;
      console.log(`Product sold!`);
    } else if (index % 2 == 0 && currentItemPrice < 10) {
      console.log(`Error in transaction!`);
    } else if (index % 2 == 0 && currentItemPrice >= 10) {
      income += currentItemPrice;
      cardSum += currentItemPrice;
      cardCount += 1;
      console.log(`Product sold!`);
    }

    if (expectedIncome <= income) {
      isMoneyGathered = true;
      break;
    }

    index++;
    command = array[index];
    
  }

  let averageCash = (cashSum / cashCount).toFixed(2);
  let averageCard = (cardSum / cardCount).toFixed(2);

  if (isMoneyGathered) {
    console.log(`Average CS: ${averageCash}`);
    console.log(`Average CC: ${averageCard}`);
  } else {
    console.log(`Failed to collect required money for charity.`);
 }
} 

vladi(["500", "120", "8", "63", "256", "78", "317"]);

vladi(["600",
"86",
"150",
"98",
"227",
"End"]);
