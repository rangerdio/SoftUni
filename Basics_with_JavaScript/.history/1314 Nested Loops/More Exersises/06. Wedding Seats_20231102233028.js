function vladi(array){
    
    let lastSector = String(array[0]);
    let rowsFirstSector = Number(array[1]);
    let oddSeatQty = Number(array[2]);

    let firstSectorNum = 65;
    let lastSectorNum = lastSector.charCodeAt(0);
    let lastRowNum = lastSectorNum +1;
    
    for (let sector = 65; sector <= lastSectorNum; sector++) {
        let sectorStr = String.fromCharCode(sector);
        
        // for (rows = rowsFirstSector; rows <= lastRowNum ; rows++) {
        
        while (condition) {
            
        
            
            if (rows % 2 ===0) {
                let oddSeats = oddSeatQty; // odd seats
            } else {
                let oddSeats = oddSeatQty + 2;// even seats
            }
            let sea = 97;
            
            for (let seat = sea; seat < (sea + oddSeatQty); seat++) {
                let seatStr = String.fromCharCode(seat);
                console.log(sectorStr + rows + seatStr);
            // end of inned loop about seats
            }
        // end of middle loop / rows
        }
            
        //end of First/ Sector Loop
    }

}

vladi(["B","3","2"]);
vladi(["C","4","2"]);