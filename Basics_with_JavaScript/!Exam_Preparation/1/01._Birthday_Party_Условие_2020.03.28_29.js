function vladi(array){
	
	let rentPrice = Number(array);
    let cake = rentPrice * 0.20;
    let drinks = cake * 0.55;
    let animator = rentPrice / 3;
    let requiredBudged = (rentPrice + cake + drinks + animator).toFixed(1);
    console.log(requiredBudged);
	
    }
   
    vladi("2250");
    vladi("3720");