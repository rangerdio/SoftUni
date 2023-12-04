function vladi(array){
	let destination = array[0];
    let dates = array[1];
    let nightQty = array[2];

    switch (destination) {
        case "France":
            switch (dates) {
                case "21-23": nightPrice = 30; break; 
                case "24-27": nightPrice = 35; break; 
                case "28-31": nightPrice = 40; break; 
            }
        break; 
        case "Italy":
            switch (dates) {
                case "21-23": nightPrice = 28; break; 
                case "24-27": nightPrice = 32; break; 
                case "28-31": nightPrice = 39; break; 
            }
        break;   
        case "Germany":
            switch (dates) {
                case "21-23": nightPrice = 32; break; 
                case "24-27": nightPrice = 37; break; 
                case "28-31": nightPrice = 43; break; 
            }
        break; 
    }
    let totalPrice = (nightQty * nightPrice).toFixed(2);
    console.log(`Easter trip to ${destination} : ${totalPrice} leva.`);
	}
   
    vladi(["Germany",
    "24-27",
    "5"])
    ;
    vladi(["Italy",
    "21-23",
    "7"])
    ;
    vladi(["France",
    "28-31",
    "8"])
    ;