function vladi(array){
	let guestsQty = Number(array[0]);
	let budged = Number(array[1]);
    let kozunakPrice = 4;
    let eggPrice = 0.45;
    let kozunakQtyNeeded = Math.ceil(guestsQty / 3);
    let neededEggs = Math.ceil(guestsQty * 2);
	let totalAmount = kozunakPrice * kozunakQtyNeeded + neededEggs * eggPrice;
    let diff = (Math.abs(totalAmount - budged)).toFixed(2);

    if (budged >= totalAmount) {
        console.log(`Lyubo bought ${kozunakQtyNeeded} Easter bread and ${neededEggs} eggs.`);
        console.log(`He has ${diff} lv. left.`);
    } else {
        console.log(`Lyubo doesn't have enough money.`);
        console.log(`He needs ${diff} lv. more.`);
    }
    }
   
    vladi(["10",
    "35"])
    ;
    vladi(["9",
    "12"])
    ;