function vladi(input){

    let poolCapacity = Number(input[0])
    let tube1Capacity = Number(input[1])
    let tube2Capacity = Number(input[2])
    let hours = Number(input[3])

    currentVolume = tube1Capacity * hours + tube2Capacity * hours
    percentage = (100 * currentVolume / poolCapacity).toFixed(2)
    percentageTube1 = (100 * tube1Capacity * hours / currentVolume).toFixed(2)
    percentageTube2 = 100 - percentageTube1
    difference = Math.abs(currentVolume - poolCapacity)

    if (currentVolume <= poolCapacity) {
        console.log(`The pool is ${percentage}% full. Pipe 1: ${percentageTube1}%. Pipe 2: ${percentageTube2}%.`);
    } else {
        console.log(`For ${hours} hours the pool overflows with ${difference} liters.`);
    }

    // console.log(percentageTube1);
    // console.log(percentageTube2);
    // console.log(percentage);
    
    };
   
    vladi([1000, 100, 120, 3]);
    vladi([100, 100, 100, 2.5]);