function vladi(input){

    celsius = Number(input[0])
    farenheit = (celsius * 1.8 + 32).toFixed(2)
    console.log(farenheit);
    }
   
    vladi([25]);
    vladi([0]);
    vladi([-5.5]);
    vladi([32.3]);