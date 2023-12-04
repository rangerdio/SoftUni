function vladi(input){

    let x = Number(input[0]);
    let y = Number(input[1]);
    let h = Number(input[2]);
    greenLforSqm = 3.4;
    redLforSqm = 4.3;
    greenArea = ( (x * x - 2 * 1.2) + x * x + 2 * (x * y - 1.5 * 1.5));
    redArea = ((x * h)) + (2 * (x * y));
    greenLiters = (greenArea / greenLforSqm).toFixed(2);
    redLiters = (redArea / redLforSqm).toFixed(2);
    console.log(greenLiters);
    console.log(redLiters);
    
    }
   
    vladi([6, 10, 5.2]);
    vladi([10.25, 15.45, 8.8]);