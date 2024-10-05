function vladi(input){

    let fuel = String(input[0]);
    let litersInTank = Number(input[1]);
    fuel = fuel.toLowerCase()

    if (fuel === "diesel" || fuel === "gasoline" || fuel === "gas") {
        if (litersInTank >= 25) {
            console.log(`You have enough ${fuel}.`);
        } else {
            console.log(`Fill your tank with ${fuel}!`);
        }
    } else if (fuel !== "diesel" && fuel !== "gasoline" && fuel !== "gas") {
        console.log(`Invalid fuel!`);
    }

    
    }
   
    // vladi(["Diesel", 10]);
    vladi(["Gasoline", 40]);
    vladi(["Gas", 25]);
    vladi(["Kerosine", 200]);