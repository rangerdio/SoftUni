function vladi(array){
	let avioCompany = array[0];
    let adult_tickets = Number(array[1]);
    let kid_tickets = Number(array[2]);
    let price_adult_ticket = Number(array[3]);
    let tax = Number(array[4]);
    let price_kid_ticket = price_adult_ticket * 0.3;
    let taxes = (adult_tickets + kid_tickets) * tax;
    let totalIncome = 0;
    let profit = 0;

    totalIncome = adult_tickets * price_adult_ticket + kid_tickets * price_kid_ticket + taxes;
    profit = (totalIncome * 0.2).toFixed(2);
    console.log(`The profit of your agency from ${avioCompany} tickets is ${profit} lv.`);   
		
    }
   
    vladi(["WizzAir",
    "15",
    "5",
    "120",
    "40"])
    ;
    vladi(["Ryanair",
    "60",
    "23",
    "158.96",
    "39.12"]);    