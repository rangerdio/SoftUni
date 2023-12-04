function vladi(input){

    let season = input[0];
    let groupType = input[1];
    let studentQty = Number(input[2]);
    let nightsQty = Number(input[3]);
    let sport = "";
    let nightPice = 0;

    switch (season) {
        case "Winter":
            switch (groupType) {
                case "girls":
                    nightPice = 9.60;
                    sport = "Gymnastics"
                    break;
                case "boys":
                    nightPice = 9.60;
                    sport = "Judo"
                    break;
                case "mixed":
                    nightPice = 10;
                    sport = "Ski"
                    break;
                default:
                    break;
            }
            break;

        case "Spring":
            switch (groupType) {
                case "girls":
                    nightPice = 7.20;
                    sport = "Athletics"
                    break;
                case "boys":
                    nightPice = 7.20;
                    sport = "Tennis"
                    break;
                case "mixed":
                    nightPice = 9.50;
                    sport = "Cycling"
                    break;
                default:
                    break;
            }
            break;

        case "Summer":
            switch (groupType) {
                case "girls":
                    nightPice = 15;
                    sport = "Volleyball"
                    break;
                case "boys":
                    nightPice = 15;
                    sport = "Football"
                    break;
                case "mixed":
                    nightPice = 20;
                    sport = "Swimming"
                    break;
                default:
                    break;
            }
            break;
        default:
            break;
    }
    let totalNightsPrice = nightPice * nightsQty * studentQty;
    if (studentQty >= 50) {
        totalNightsPrice *= 0.50;
    } else if (studentQty >= 20 && studentQty < 50) {
        totalNightsPrice *= 0.85;
    } else if (studentQty >= 10 && studentQty < 20) {
        totalNightsPrice *= 0.95;
    }
    totalNightsPrice = (totalNightsPrice).toFixed(2);
    console.log(`${sport} ${totalNightsPrice} lv.`);
    }

    vladi(["Spring", "girls", "20", "7"]);
    vladi(["Winter", "mixed", "9", "15"]);
    vladi(["Summer", "boys", "60", "7"]);
    vladi(["Spring", "mixed", "17", "14"]);