function vladi(array){
    let numbers = Number(array[0]);
    let oddSum = 0; let oddMin = 0; let oddMax = 0; let evenSum = 0; let evenMin = 0; let evenMax = 0;
    let oddMinPrevious = 0; let oddMaxPrevious = 0; let evenMinPrevious = 0; let evenMaxPrevious = 0;
    isOddNo = false; isEvenNo = false;

    if (numbers === 0) {isOddNo = true}
    if (numbers === 1) {isEvenNo = true}

    for (let i = 1; i <= numbers; i++) {
        currentNumber = Number(array[i]);

        if (i === 1) {
            oddSum += currentNumber; oddMaxPrevious = currentNumber; oddMinPrevious = currentNumber;
        } else if (i % 2 !==0) {
            oddSum += currentNumber;
            if (currentNumber >= oddMaxPrevious) {oddMaxPrevious = currentNumber;}
            if (currentNumber <= oddMinPrevious) {oddMinPrevious = currentNumber;}
        } else if (i === 2) {
            evenSum += currentNumber; evenMaxPrevious = currentNumber; evenMinPrevious = currentNumber;
        } else if (i % 2 === 0) {
            evenSum += currentNumber;
                if (currentNumber >= evenMaxPrevious) {evenMaxPrevious = currentNumber;}
                if (currentNumber <= evenMinPrevious) {evenMinPrevious = currentNumber;}
        }
    }
    
    oddSum = (oddSum).toFixed(2);
    oddMax = (oddMaxPrevious).toFixed(2);
    oddMin = (oddMinPrevious).toFixed(2);   
    evenSum = (evenSum).toFixed(2);
    evenMax = (evenMaxPrevious).toFixed(2);
    evenMin = (evenMinPrevious).toFixed(2);

    if (isOddNo) { oddMin = "No"; oddMax = "No"; evenMin = "No"; evenMax = "No";}
    if (isEvenNo) { evenMin = "No"; evenMax = "No";}

    console.log(`OddSum=${oddSum},`);
    console.log(`OddMin=${oddMin},`);
    console.log(`OddMax=${oddMax},`);
    console.log(`EvenSum=${evenSum},`);
    console.log(`EvenMin=${evenMin},`);
    console.log(`EvenMax=${evenMax}`);
}
    vladi(["6", "2", "3", "5", "4", "2", "1"]);
    // vladi(["5", "3", "-2", "8", "11", "-3"]);
    // vladi(["2", "1.5", "-2.5"]);
    // vladi(["4", "1.5", "1.75", "1.5", "1.75"]);
    // vladi(["1", "1"]);
    // vladi(["1", "5"]);
    // vladi(["0"]);
    // vladi(["3", "-1", "-2", "-3"]);