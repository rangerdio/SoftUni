function vladi(array){
	let eggSize = array[0];
	let eggColor = array[1];
	let seriesQty = Number(array[2]);
    let finalPrice = 0;
    let price = 0;
	
    switch (eggSize) {
        case "Large":
            
            switch (eggColor) {
                case "Red": price = 16; break; 
                case "Green": price = 12; break; 
                case "Yellow": price = 9; break; 
            }

        break;
        case "Medium":
            
            switch (eggColor) {
                case "Red": price = 13; break; 
                case "Green": price = 9; break; 
                case "Yellow": price = 7; break; 
        }

        break;
        case "Small":
            
            switch (eggColor) {
                case "Red": price = 9; break; 
                case "Green": price = 8; break; 
                case "Yellow": price = 5; break; 
        }

        break;
    }
    finalPrice = seriesQty * price;
    finalPrice = (finalPrice * 0.65).toFixed(2); // without manufacture expenses
	console.log(`${finalPrice} leva.`);
    }
   
    vladi(["Large",
    "Red",
    "7"])
    ;
    vladi(["Medium",
    "Green",
    "5"])
    ;
    vladi(["Small",
    "Yellow",
    "3"])
    ;