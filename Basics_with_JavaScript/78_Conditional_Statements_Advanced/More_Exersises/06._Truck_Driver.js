function vladi(input){

    let season = input[0]
    let distancePerMonth = Number(input[1])
    let pricePerKm = 0

    if (distancePerMonth <= 5000) {
        switch (season) {
            case "Spring":
            case "Autumn":
                pricePerKm = 0.75;
                break;
            case "Summer":
                pricePerKm = 0.90;
                break;
            case "Winter":
                pricePerKm = 1.05;
                break;
            default:
                break;
        }
    } else if (distancePerMonth > 5000 && distancePerMonth <= 10000) {
        switch (season) {
            case "Spring":
            case "Autumn":
                pricePerKm = 0.95;
                break;
            case "Summer":
                pricePerKm = 1.10;
                break;
            case "Winter":
                pricePerKm = 1.25;
                break;
            default:
                break;
        }
    } else if (distancePerMonth > 10000 && distancePerMonth <= 20000) {
        pricePerKm = 1.45;
    }
    let salary = ((4 * distancePerMonth * pricePerKm)* 0.9).toFixed(2)
    console.log(salary);
    }
   
    vladi(["Summer", "3455"]);
    vladi(["Winter", "4350"]);
    vladi(["Spring", "1600"]);
    vladi(["Winter", "5678"]);
    vladi(["Autumn", "8600"]);
    vladi(["Winter", "16042"]);
    vladi(["Spring", "16942"]);