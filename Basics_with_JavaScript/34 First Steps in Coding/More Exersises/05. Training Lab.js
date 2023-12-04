function vladi(input){

    let wm = Number(input[0])
    let hm = Number(input[1])
    w = wm * 100
    h = hm * 100
    losses = 3
    corridor = 100
    h = h - corridor
    seatH = 70
    seatW = 120
    collons = Math.floor(w / seatW)
    rows = Math.floor(h / seatH)
    maxSeats = Math.floor(rows * collons - losses)

    console.log(maxSeats);
    
    }
   
    vladi([15, 8.9]);
    vladi([8.4, 5.2]);