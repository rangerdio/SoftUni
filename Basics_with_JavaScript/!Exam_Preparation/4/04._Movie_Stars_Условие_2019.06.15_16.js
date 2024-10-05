function vladi(array){
	let budged = Number(array[0]);
    let actorExpense = 0;
    isSkipp = false;
    isNoMoney = false;
    let k = 0;

    for (let  i = 1;  i < array.length;  i++) {



     if (actorName === "ACTION") {
        break;
     } else if (actorName.length > 15) {
        actorExpense = budged * 0.20;
        budged -= actorExpense

        if (budged < 0) {isNoMoney = true; break;}
     } else { 
        if (isSkipp) {
            k = i + 1;
        actorExpense = Number(array[i + 1]);
        
        if (budged < 0) {isNoMoney = true; break;}
     }
    
    }
	
    }

    if (isNoMoney) {
        budged = (Math.abs(budged).toFixed(2));
        console.log(`We need ${budged} leva for our actors.`);
    }

    budged = budged.toFixed(2);
    console.log(`We are left with ${budged} leva.`);
}   
    vladi(["90000",
    "Christian Bale",
    "70000.50",
    "Leonard DiCaprio",
    "Kevin Spacey",
    "24000.99"])
    ;
    vladi(["170000",
    "Ben Affleck",
    "40000.50",
    "Zahari Baharov",
    "80000",
    "Tom Hanks",
    "2000.99",
    "ACTION"])
    ;