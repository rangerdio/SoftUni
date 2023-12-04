function vladi(input){

    let radius = Number(input[0]);
    area = (radius *radius * Math.PI).toFixed(2);
    perimeter = (radius * 2 * Math.PI).toFixed(2);
    console.log(area);
    console.log(perimeter);
    }
   
    vladi([3]);
    vladi([4.5]);