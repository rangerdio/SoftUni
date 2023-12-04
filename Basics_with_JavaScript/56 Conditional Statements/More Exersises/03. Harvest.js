function vladi(input) {
  let lozeArea = Number(input[0]);
  let grapesPerSqm = Number(input[1]);
  let wineNeeds = Number(input[2]);
  let workersQuantity = Number(input[3]);
  let lozeForWineProduction = lozeArea * 0.4;

  let wineProducedL = (lozeForWineProduction * grapesPerSqm) / 2.5;

  difference1 = Math.floor(Math.abs(wineNeeds - wineProducedL));
  difference2 = Math.ceil(Math.abs(wineNeeds - wineProducedL));
  let workerWine = Math.ceil(difference2 / workersQuantity);

  if (wineProducedL < wineNeeds) {
    console.log(
      `It will be a tough winter! More ${difference1} liters wine needed.`
    );
  } else {
    console.log(`Good harvest this year! Total wine: ${wineProducedL} liters.`);
    console.log(
      `${difference2} liters left -> ${workerWine} liters per person.`
    );
  }
}

vladi([650, 2, 175, 3]);
vladi([1020, 1.5, 425, 4]);
