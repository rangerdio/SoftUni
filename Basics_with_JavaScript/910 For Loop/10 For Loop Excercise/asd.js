function vladi(){


    
    }
   
    vladi();


    if (i === 1) {
        oddSum = currentNumber; oddMaxPrevious = currentNumber; oddMinPrevious = currentNumber;
    } else if (i % 2 !==0) {
        oddSum += currentNumber;
        if (currentNumber >= oddMaxPrevious) {oddMaxPrevious = currentNumber;}
        if (currentNumber <= oddMinPrevious) {oddMinPrevious = currentNumber;}
    } else if (i === 2) {
        evenSum = currentNumber; evenMaxPrevious = currentNumber; evenMinPrevious = currentNumber;
    } else if (i % 2 === 0) {
        evenSum += currentNumber;
            if (currentNumber >= evenMaxPrevious) {evenMaxPrevious = currentNumber;}
            if (currentNumber <= evenMinPrevious) {evenMinPrevious = currentNumber;}
    }
    
    
    
    
    


