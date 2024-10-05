function vladi(input){

    let budged = Number(input[0]);
    let category = input[1];
    let groupQty = Number(input[2])
    let transport = 0
    let tickets = 0
    let newBudged = 0
    let ticketPrice = 0
    let diff = 0

    if (groupQty >= 1 && groupQty <= 4) {
        transport = budged * 0.75;
    } else if (groupQty >= 5 && groupQty <= 9) {
        transport = budged * 0.60;
    } else if (groupQty >= 10 && groupQty <= 24) {
        transport = budged * 0.50;
    } else if (groupQty >= 25 && groupQty <= 49) {
        transport = budged * 0.40;
    } else if (groupQty >= 50) {
        transport = budged * 0.25;
        
    }

    newBudged = budged - transport;
    switch (category) {
        case "Normal":
            ticketPrice = 249.99
            break;
        case "VIP":
            ticketPrice = 499.99
            break;
    }

    tickets = ticketPrice * groupQty
    diff = (Math.abs(tickets - newBudged)).toFixed(2)

    if (newBudged >= tickets) {
        console.log(`Yes! You have ${diff} leva left.`); 
    } else {
        console.log(`Not enough money! You need ${diff} leva.`);
    }

    }
    vladi(["1000", "Normal", "1"]);
    vladi(["30000", "VIP", "49"]);