function vladi(array){
	
	let luggagePriceAfter20 = Number(array[0]);
	let luggageWeight = Number(array[1]);
	let daysTillTrip = Number(array[2]);
	let luggageQty = Number(array[3]);
    let bagPrice = 0;
    

    if (luggageWeight <10) {
        bagPrice = luggagePriceAfter20 * 0.20;
    } else if (luggageWeight >= 10 && luggageWeight <= 20) {
        bagPrice = luggagePriceAfter20 * 0.50;
    } else {
        bagPrice = luggagePriceAfter20;
    }
        bagPrice *= luggageQty;

    if (daysTillTrip > 30) {
        bagPrice *= 1.10;
    } else if (daysTillTrip >= 7 && daysTillTrip <= 30) {
        bagPrice *= 1.15;
    } else if (daysTillTrip < 7) {
        bagPrice *= 1.40;
    }
	bagPrice = (bagPrice).toFixed(2);
    console.log(`The total price of bags is: ${bagPrice} lv.`);
    }
   
    vladi(["30",
    "18",
    "15",
    "2"])
    ;
    vladi(["25.50",
    "5",
    "36",
    "6"])
    ;
    vladi(["63.80",
    "23",
    "3",
    "1"])
    ;