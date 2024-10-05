function vladi(input){

    let days = Number(input[0]);
    let availableFood = Number(input[1]);
    let dogPerDay = Number(input[2]);
    let catPerDay = Number(input[3]);
    let turtlePerDayGrams = Number(input[4]);
    let turtlePerDay = turtlePerDayGrams / 1000;

    let neededFood = Math.ceil((dogPerDay + catPerDay + turtlePerDay) * days)
    let difference = Math.ceil(Math.abs(availableFood - neededFood))
    
    if (availableFood >= neededFood) {
        console.log(`${difference} kilos of food left.`);
    } else {
        console.log(`${difference} more kilos of food are needed.`);
    }
    }

    vladi(["2", "10", "1", "1", "1200"]);
    vladi(["5", "10", "2.1", "0.8", "321"]);