function vladi(array) {
  let monthsQty = Number(array[0]);
  let totalBills = 0;
  let electricity = 0;
  let water = 0;
  let internet = 0;
  let other = 0;
  let average = 0;
  let sum = 0;

  for (let i = 1; i <= monthsQty; i++) {
    currentElectricity = Number(array[i]);
    electricity += currentElectricity;
    water += 20;
    internet += 15;
    other += (currentElectricity + 20 + 15) * 1.2;
  }
  totalBills = electricity + water + internet + other;
  average = (totalBills / monthsQty).toFixed(2);

  console.log(`Electricity: ${electricity.toFixed(2)} lv`);
  console.log(`Water: ${water.toFixed(2)} lv`);
  console.log(`Internet: ${internet.toFixed(2)} lv`);
  console.log(`Other: ${other.toFixed(2)} lv`);
  console.log(`Average: ${average} lv`);
}

vladi(["5", "68.63", "89.25", "132.53", "93.53", "63.22"]);
vladi(["8", "123.54", "231.54", "140.23", "100", "122.4", "430", "178.52", "64.2"]);
