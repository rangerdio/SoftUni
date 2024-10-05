function vladi(array){
    isNoCapacity = false;
    let bottlesQty = Number(array[0]);
    let capacity = bottlesQty * 750;
    let sudove = 0;
    let potCount = 0;
    let dishCount = 0;
    
    let index = 0;
    index++;
    let command = array[index];
    
    

    while (command !== "End") {
        sudove = Number(command);
        if (index % 3 == 0) {
            capacity -= sudove * 15;
            potCount += sudove;
        } else {
            capacity -= sudove * 5;
            dishCount += sudove;
        }
        if (capacity < 0) {
            isNoCapacity = true
            break;
        }
        index++;
        command = array[index];
    }
    diff = Math.abs(capacity);

    if (isNoCapacity) {
        console.log(`Not enough detergent, ${diff} ml. more necessary!`);
    } else {
        console.log(`Detergent was enough!`);
        console.log(`${dishCount} dishes and ${potCount} pots were washed.`);
        console.log(`Leftover detergent ${capacity} ml.`);
    }
    }
   
    // vladi(["2",
    // "53",
    // "65",
    // "55",
    // "End"]);
    vladi(["1",
    "10",
    "15",
    "10",
    "12",
    "13",
    "30"]);
