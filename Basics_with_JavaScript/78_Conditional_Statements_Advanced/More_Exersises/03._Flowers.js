function vladi(input){

    let hrizQty = Number(input[0])
    let rosesQty = Number(input[1])
    let laleQty = Number(input[2])
    let season = (input[3])
    let command = (input[4])
    let rosesPrice = 0
    let hrizPrice = 0
    let lalePrice = 0
    let priceFlowers = 0
    switch (season) {
        case "Spring":
        case "Summer":
            hrizPrice = 2.00
            rosesPrice = 4.10
            lalePrice = 2.5
            break;
        case "Autumn":
        case "Winter":
            hrizPrice = 3.75
            rosesPrice = 4.50
            lalePrice = 4.15
            break
    }
    
    priceFlowers = hrizPrice * hrizQty + rosesPrice * rosesQty + lalePrice * laleQty
    if (command === "Y") {
        priceFlowers *= 1.15
    }
    if (season === "Spring" && laleQty > 7) {
        priceFlowers *= 0.95
    } else if (season === "Winter" && rosesQty >= 10) {
        priceFlowers *= 0.90
    }
    if (laleQty + rosesQty + hrizQty > 20) {
        priceFlowers *= 0.80
    }
     priceFlowers += 2
     priceFlowers = priceFlowers.toFixed(2)
     console.log(priceFlowers);
    }
   
    vladi(["2","4","8","Spring","Y"]);
    vladi(["3","10","9","Winter","N"]);
    vladi(["10","10","10","Autumn","N"]);