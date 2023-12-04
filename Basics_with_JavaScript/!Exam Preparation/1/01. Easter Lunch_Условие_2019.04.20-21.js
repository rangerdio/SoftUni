function vladi(array){
	
	let kozunakQty = Number(array[0]);
	let eggPacks = Number(array[1]);
	let kurabiiKg = Number(array[2]);
    let kozunakPrice = 3.20;
    let eggPackPrice = 4.35;
    let kurabiiKgPrice = 5.40;
    let eggPaintPerEgg = 0.15;

    let kozunakAmount = kozunakPrice * kozunakQty;
    let eggsAmount = eggPacks * eggPackPrice;
    let kurabAmount = kurabiiKg * kurabiiKgPrice;
    let paintAmount = eggPacks * 12 * 0.15;
    let totalAmount = (kozunakAmount + kurabAmount + paintAmount + eggsAmount).toFixed(2)
    console.log(totalAmount);
	
    }
   
    vladi(["3",
    "2",
    "3"])
    ;
    vladi(["4",
    "4",
    "3"])
    ;