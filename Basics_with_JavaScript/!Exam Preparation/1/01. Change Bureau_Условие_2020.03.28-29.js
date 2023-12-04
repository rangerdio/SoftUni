function vladi(array){
	
	let bitCoinQty = Number(array[0]);
	let ioanQty = Number(array[1]);
	let commission = Number(array[2]);
    let lvBitCoins = bitCoinQty * 1168
    let usdIoans = ioanQty * 0.15;
    let lvIoans = usdIoans * 1.76
    let lvtotal  = lvBitCoins + lvIoans;
    let euros =  lvtotal  / 1.95;


    let eurosCom = (euros * (100 - commission) / 100).toFixed(2);
	console.log(eurosCom);
    }
   
    vladi(["1",
    "5",
    "5"])
    ;
    vladi(["20",
    "5678",
    "2.4"])
    ;
    vladi(["7",
    "50200.12",
    "3"])
    ;