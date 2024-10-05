function vladi(array){
	let drinkType = array[0];
    let sugarType = array[1];
    let qty = Number(array[2]);
    let price = 0;

    switch (drinkType) {
        case "Espresso":
            
            switch (sugarType) {  
                case "Without": price = 0.90; break;
                case "Normal": price = 1; break;
                case "Extra": price = 1.20; break;
            }
            break;
        case "Cappuccino":
            
            switch (sugarType) {  
                case "Without": price = 1; break;
                case "Normal": price = 1.20; break;
                case "Extra": price = 1.60; break;
            }
            break;

        case "Tea":
            
            switch (sugarType) {  
                case "Without": price = 0.50; break;
                case "Normal": price = 0.60; break;
                case "Extra": price = 0.70; break;
            }
            break;
    }

    let total = qty * price;

    if (sugarType === "Without") {
        total *= 0.65;
    } 
    if (drinkType === "Espresso" && qty >= 5 ) {
        total *= 0.75;
    }
    
    if (total > 15) {
        total *= 0.80;
    }

    total = total.toFixed(2);

    console.log(`You bought ${qty} cups of ${drinkType} for ${total} lv.`);

    }
   
    vladi(["Espresso",
    "Without",
    "10"])
    ;
    vladi((["Cappuccino",
    "Normal",
    "13"])
    );
    vladi(["Tea",
    "Extra",
    "3"])
    ;