function vladi(input){

    let weather = String(input[0]);
    if (weather == "sunny") {
        console.log("It's warm outside!"); } 
    else {
        console.log("It's cold outside!"); }
    }
   
    vladi(["sunny"]);
    vladi(["cloudy"]);
    vladi(["snowy"]);