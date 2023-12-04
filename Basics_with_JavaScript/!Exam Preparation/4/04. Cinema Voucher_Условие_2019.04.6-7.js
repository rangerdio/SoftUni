function vladi(array){
	let voucherPrice = Number(array[0]);
    let price = 0; 
    let ticketCount = 0;
    let otherCount = 0;
    
    for (let i = 1; i < array.length ; i++) {
        let present = array[i];

        if (present === "End") {
            break;
        }
        if (present.length > 8) {
            price = (present.charCodeAt(0) + present.charCodeAt(1));
            if (price > voucherPrice) {
                   break
            }
            ticketCount += 1;
        } else {
            price = present.charCodeAt(0);
            if (price > voucherPrice) {
                break
            }
            otherCount += 1;
        }
        voucherPrice -= price;
         
    }
    console.log(ticketCount);
    console.log(otherCount)
    }

    vladi(["300","Captain Marvel","popcorn","Pepsi"]);
    vladi(["1500","Avengers: Endgame","Bohemian Rhapsody","Deadpool 2","End"]);