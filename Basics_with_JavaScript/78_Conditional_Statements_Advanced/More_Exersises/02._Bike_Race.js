function vladi(input){

    let juniors = Number(input[0]);
    let seniors = Number(input[1]);
    let type = input[2];
    let income = 0
    let juniorTax = 0
    let seniorTax = 0

    switch (type) {
        case "trail":
            juniorTax = 5.50;
            seniorTax = 7;
            break;
        case "cross-country":
            juniorTax = 8;
            seniorTax = 9.50;
            break;
        case "downhill":
            juniorTax = 12.25;
            seniorTax = 13.75;
            break;
        case "road":
            juniorTax = 20;
            seniorTax = 21.50;
            break;
    }
    income = juniorTax * juniors + seniorTax * seniors
    if (type == "cross-country" && (seniors + juniors >= 50)) {
        income *= 0.75
    }
    income = (income * 0.95).toFixed(2)
    
    console.log(income);
    
    }

    vladi(["10", "20", "trail"]);
    vladi(["21", "26", "cross-country"]);
    vladi(["30", "25", "cross-country"]);
    vladi(["10", "10", "downhill"]);
    vladi(["3", "40", "road"]);