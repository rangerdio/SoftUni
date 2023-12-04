function vladi(array){
	
	let guests = Number(array[0]);
	let kuvert = Number(array[1]);
	let budged = Number(array[2]);
    let cake = budged * 0.10;
    let total = 0; discount = 0;

    if (guests >= 10 && guests <= 15) {
        discount = 15;
    } else if (guests > 15 && guests <= 20) {
        discount = 20;
    } else if (guests > 20) {
        discount = 25;
    }
    kuvert = kuvert * (100 - discount) / 100;
    total = kuvert * guests + cake;
    let diff = (Math.abs(total - budged)).toFixed(2);
    if (total <= budged) {
        console.log(`It is party time! ${diff} leva left.`);
    } else {console.log(`No party! ${diff} leva needed.`);}
	
    }
   
    vladi(["18",
    "30",
    "450"])
    ;
    vladi(["8",
    "25",
    "340"])
    ;
    vladi(["24",
    "35",
    "550"])
    ;