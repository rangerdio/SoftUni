function vladi(input) {
  let gasolinePrise = 2.22;
  let dieselPrice = 2.33;
  let gasPrice = 0.93;
  let fuelType = String(input[0]);
  let liters = Number(input[1]);
  let command = String(input[2]);
  let price = 0;

  if (command === "Yes") {
    gasolinePrise -= 0.18;
    dieselPrice -= 0.12;
    gasPrice -= 0.08;
  }

  if (fuelType === "Gas") {
    price = gasPrice;
  } else if (fuelType === "Gasoline") {
    price = gasolinePrise;
  } else if (fuelType === "Diesel") {
    price = dieselPrice;
  }
  let bill = price * liters;
  if (liters >= 20 && liters <= 25) {
    bill *= 0.92;
  } else if (liters > 25) {
    bill *= 0.9;
  }
  bill = bill.toFixed(2);
  console.log(`${bill} lv.`);
}

vladi(["Gas", "30", "Yes"]);
vladi(["Gasoline", "25", "No"]);
vladi(["Diesel", "19", "No"]);
