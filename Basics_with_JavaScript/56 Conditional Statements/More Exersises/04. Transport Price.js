function vladi(input) {
  let distance = Number(input[0]);
  let command = String(input[1]);
  let taxiPrice = 0;
  let busPrice = 0;
  let trainPrice = 0;
  buss = false;
  train = false;
  let lowest = 0;
  let taxiPricePerKm = 0

  if (command == "day") {
    taxiPricePerKm = 0.79;
  } else if (command == "night") {
    taxiPricePerKm = 0.9;
  }

  let busPricePerKm = 0.09;
  let trainPricePerKm = 0.06;
  taxiPrice = distance * taxiPricePerKm + 0.7;
  busPrice = busPricePerKm * distance;
  trainPrice = trainPricePerKm * distance;

  if (distance < 20) {
    lowest = taxiPrice;
  } else if (distance >= 20 && distance < 100) {
    if (taxiPrice <= busPrice) {
      lowest = taxiPrice;
    } else {
      lowest = busPrice;
    }
  } else if (distance >= 100) {
    if (taxiPrice <= busPrice && taxiPrice <= trainPrice) {
      lowest = taxiPrice;
    } else if (taxiPrice <= busPrice && taxiPrice > trainPrice) {
      lowest = trainPrice;
    } else if (taxiPrice > busPrice && busPrice <= trainPrice) {
      lowest = busPrice;
    } else if (taxiPrice > busPrice && busPrice > trainPrice) {
      lowest = trainPrice;
    }
  }
  lowest = lowest.toFixed(2);

  console.log(lowest);
}

vladi(["5", "day"]);
vladi(["7", "night"]);
vladi(["25", "day"]);
vladi(["180", "night"]);
