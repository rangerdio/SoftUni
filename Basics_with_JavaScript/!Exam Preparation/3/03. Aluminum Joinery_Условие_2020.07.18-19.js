function vladi(array){
	let qty = Number(array[0]);
    let size = array[1];
	let deliveryType = array[2];
    let price = 0;
    let discount = 0;
    let deliveryPrice = 60;

    if (qty < 10) {
        console.log(`Invalid order`);
    } else {

    switch (size) {
        case "90X130":
            price = 110;
            if (qty > 30 && qty <= 60) {
                discount = 0.05;
            } else if (qty > 60) {
                discount = 0.08;
            }


        break;
            
        case "100X150":
            price = 140;
            if (qty > 40 && qty <= 80) {
                discount = 0.06;
            } else if (qty > 80) {
                discount = 0.10;
            }

            break;

        case "130X180":
            price = 190;
            if (qty > 20 && qty <= 50) {
                discount = 0.07;
            } else if (qty > 50) {
                discount = 0.12;
            }

            break;

        case "200X300":
            price = 250;
            if (qty > 25 && qty <= 50) {
                discount = 0.09;
            } else if (qty > 50) {
                discount = 0.14;
            }

            break;
    }
    let discountedPrice = qty * ( price * (1 - discount) );


    
    switch (deliveryType) {
        case "With delivery":
            discountedPrice += 60;
            break;
        default:
            break;
    }

    if (qty > 99) {
        discountedPrice = discountedPrice * 0.96;
    }

    discountedPrice = (discountedPrice).toFixed(2);

    console.log(`${discountedPrice} BGN`);

    }

    }
   
    vladi(["40", 
    "90X130",
    "Without delivery"])
    ;
    vladi(["105",
    "100X150",
    "With delivery"])
    ;
    vladi(["2",
    "130X180",
    "With delivery"])
    ;