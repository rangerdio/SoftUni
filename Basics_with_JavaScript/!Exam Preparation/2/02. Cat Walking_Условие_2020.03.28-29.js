function vladi(array){
	let walkingMinutes = Number(array[0]);
	let dailyQty = Number(array[1]);
	let dailyCalories = Number(array[2]);
    let minWalking = dailyCalories / 2;
    let totalWalkingC = walkingMinutes * dailyQty  * 5 ;
    if (totalWalkingC >= minWalking) {
        console.log(`Yes, the walk for your cat is enough. Burned calories per day: ${totalWalkingC}.`);
    } else {console.log(`No, the walk for your cat is not enough. Burned calories per day: ${totalWalkingC}.`);}
    }
   
    vladi(["30",
    "3",
    "600"])
    ;
    vladi(["15",
    "2",
    "500"])
    ;