function vladi(input){

    let budged = Number(input[0])
    let season = (input[1])
    let classCar = ""
    let typeCar = ""
    let priceCarPercentFromBudged = 0
    let priceCar = 0
    
    if (budged<= 100) {
        classCar = "Economy class";
        switch (season) {
            case "Summer":
                typeCar = "Cabrio";
                priceCarPercentFromBudged = 35;
                break;
            case "Winter":
                typeCar = "Jeep";
                priceCarPercentFromBudged = 65;
                break;
        }
    } else if (budged > 100 && budged <= 500) {
        classCar = `Compact class`;
                if (season === "Summer") {
                    typeCar = "Cabrio";
                    priceCarPercentFromBudged = 45;
                } else if (season === "Winter") {
                    typeCar = "Jeep";
                    priceCarPercentFromBudged = 80;
                }
    } else if (budged > 500) {
        classCar = "Luxury class";
        typeCar = "Jeep";
        priceCarPercentFromBudged = 90;
    }

    priceCar = (budged * priceCarPercentFromBudged / 100).toFixed(2);

    console.log(classCar);
    console.log(`${typeCar} - ${priceCar}`);

    }
   
    vladi(["450","Summer"]);
    vladi(["450","Winter"]);
    vladi(["1010","Summer"]);
    vladi(["99.99","Summer"]);
    vladi(["1010","Winter"]);
    vladi(["70.50","Winter"]);