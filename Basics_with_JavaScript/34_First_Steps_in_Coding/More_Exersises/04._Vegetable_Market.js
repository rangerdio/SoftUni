function vladi(input){

    let priceKgVegetables = Number(input[0])
    let priceKgFruits = Number(input[1])
    let kgVegetables = Number(input[2])
    let kgFruits = Number(input[3])
    toEuro = 1 / 1.94

    total = ((priceKgFruits * kgFruits + priceKgVegetables * kgVegetables) * toEuro).toFixed(2)
    console.log(total);

    }
   
    vladi([0.194, 19.4, 10, 10]);
    vladi([1.5, 2.5, 10, 10]);