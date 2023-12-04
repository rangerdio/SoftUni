function vladi(input){

    let magnolia = 3.25, zumbul = 4, rose = 3.5, cactus = 8;
    let magnoliaQuantity = Number(input[0])
    let zumbulQuantity = Number(input[1])
    let roseQuantity = Number(input[2])
    let cactusQuantity = Number(input[3])
    let presentPrice = Number(input[4])
    let total = magnolia * magnoliaQuantity + zumbul * zumbulQuantity + rose * roseQuantity + cactus * cactusQuantity
    total = 0.95 * total
    let difference = Math.abs(total - presentPrice)
    if (total >= presentPrice) {
        difference = Math.floor(difference)
        console.log(`She is left with ${difference} leva.`);
    } else {
        difference = Math.ceil(difference)
        console.log(`She will have to borrow ${difference} leva.`);
    }

    }
   
    vladi([2,3,5,1,50]);
    vladi([15,7,5,10,100]);