function vladi(array){
    let change = Number(array[0]);
    let changeCoins = Math.trunc(change * 100);
    //let two = 0; let one = 0; let fiftyCoins = 0; let twentyCoins = 0; let tenCoins = 0; let fiveCoins = 0; let twoCoins = 0;  let oneCoins = 0;
    let counter = 0;


    while (changeCoins > 0) {
        if (changeCoins >= 200) {
            counter += Math.trunc(changeCoins / 200);
            changeCoins = changeCoins % 200;
        } else if (changeCoins >= 100) {
            counter += Math.trunc(changeCoins / 100);
            changeCoins = changeCoins % 100;
        } else if (changeCoins >= 50) {
            counter += Math.trunc(changeCoins / 50);
            changeCoins = changeCoins % 50;
        } else if (changeCoins >= 20) {
            counter += Math.trunc(changeCoins / 20);
            changeCoins = changeCoins % 20;
        } else if (changeCoins >= 10) {
            counter += Math.trunc(changeCoins / 10);
            changeCoins = changeCoins % 10;
        } else if (changeCoins >= 5) {
            counter += Math.trunc(changeCoins / 5);
            changeCoins = changeCoins % 5;
        } else if (changeCoins >= 2) {
            counter += Math.trunc(changeCoins / 2);
            changeCoins = changeCoins % 2;
        } else if (changeCoins >= 1) {
            counter += Math.trunc(changeCoins / 1);
            changeCoins = changeCoins % 1;
        }

    }
    console.log(counter);


    }
   
    // vladi(["1.23"]);
    // vladi(["2"]);
    vladi(["0.56"]);
    vladi(["2.73"]);