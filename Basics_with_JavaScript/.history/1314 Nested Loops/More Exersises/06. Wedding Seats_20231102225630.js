function vladi(array){
    
    let lastSector = String(array[0]);
    let rowsFirstSector = Number(array[1]);
    let oddSeatQty = Number(array[2]);

    let firstSectorNum = 65;
    let lastSectorNum = lastSector.charCodeAt(0);
    let lastRowNum = lastSectorNum - firstSectorNum;
    
    for (let sector = 65; sector <= lastSectorNum; sector++) {
        let sectorStr = String.fromCharCode(sector);
        
        for (rows = rowsFirstSector; rows <= lastRowNum ; rows++) {
            let rowsStr = String.fromCharCode(rows);
            
            if (rows % 2 ===0) {
                let oddSeats = oddSeatQty; // odd seats
            } else {
                let oddSeats = oddSeatQty + 2;// even seats
            }
            
            for (let seat = 97; seat < seat + oddSeatQty; seat++); {
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