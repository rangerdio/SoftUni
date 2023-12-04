function vladi(array){
	
	let flourPricePerKg = Number(array[0]);
	let flourQty = Number(array[1]);
	let sugarQty = Number(array[2]);
	let eggPacks = Number(array[3]);
	let yeastPacks = Number(array[4]);
    let sugarPerKgPrice = flourPricePerKg * 0.75;
    let eggPackPrice = flourPricePerKg * 1.10;
    let yeastPackPrice = sugarPerKgPrice * 0.20;

    let neededAmount = (flourPricePerKg * flourQty + sugarPerKgPrice * sugarQty + eggPackPrice * eggPacks + yeastPackPrice * yeastPacks).toFixed(2);
    console.log(neededAmount);
	
    }
   
    vladi(["50",
    "10",
    "3.5",
    "6",
    "1"])
    ;
    vladi(["63.44",
    "3.57",
    "6.35",
    "8",
    "2"])
    ;