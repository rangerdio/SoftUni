function vladi(array){
    let capacity = Number(array[0]);
    let fans = Number(array[1]);
    let aQty = 0; let bQty = 0; let vQty = 0; let gQty = 0;

    for (let i = 2; i <= fans + 1; i++) {
        let sector = array[i];
        switch (sector) {
            case "A": aQty += 1; break;
            case "B": bQty += 1; break;
            case "V": vQty += 1; break;
            case "G": gQty += 1; break;
        }
    }
    
    aQty = (100 * aQty / fans).toFixed(2);
    bQty = (100 * bQty / fans).toFixed(2);
    vQty = (100 * vQty / fans).toFixed(2);
    gQty = (100 * gQty / fans).toFixed(2);
    let sumPerStadium = (100 * fans / capacity).toFixed(2);
    console.log(`${aQty}%`);
    console.log(`${bQty}%`);
    console.log(`${vQty}%`);
    console.log(`${gQty}%`);
    console.log(`${sumPerStadium}%`);
    }
   
    vladi(["76", "10", "A", "V", "V", "V", "G", "B", "A","V","B","B"]);
    vladi(["93", "16", "A", "V", "G", "G", "B", "B", "G","B","A","B", "B", "B", "A","B","B","A"]);