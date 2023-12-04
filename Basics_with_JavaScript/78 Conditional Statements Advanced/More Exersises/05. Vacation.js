function vladi(input){

    let budged = Number(input[0]);
    let season = input[1];
    let location = "";
    let typeHouse = "";
    let price = 0;
    let pricePercentFromBudged = 0

    if (budged <= 1000) {
        typeHouse = "Camp";
        switch (season) {
            case "Summer":
                location = "Alaska";
                pricePercentFromBudged = 65;
                break;
            case "Winter":
                location = "Morocco";
                pricePercentFromBudged = 45
                break;
            default:
                break;
        }
    } else if (budged > 100 && budged <= 3000) {
        typeHouse = "Hut";
        switch (season) {
            case "Summer":
                location = "Alaska";
                pricePercentFromBudged = 80    
                break;
            case "Winter":
                location = "Morocco";
                pricePercentFromBudged = 60;
                break;
            default:
                break;
        }
    } else if (budged > 3000) {
        typeHouse = "Hotel";
        pricePercentFromBudged = 90
        switch (season) {
            case "Summer":
                location = "Alaska";
                break;
            case "Winter":
                location = "Morocco";
                break;
            default:
                break;
        }
    }

    
    price = (budged * (pricePercentFromBudged / 100)).toFixed(2)
    console.log(`${location} - ${typeHouse} - ${price}`);
    }
   
    vladi(["800", "Summer"]);
    vladi(["799.50", "Winter"]);
    vladi(["3460", "Summer"]);
    vladi(["1100", "Summer"]);
    vladi(["5000", "Winter"]);
    vladi(["2543.99", "Winter"]);