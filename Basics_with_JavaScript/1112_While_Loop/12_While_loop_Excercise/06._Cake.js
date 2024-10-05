function vladi(array){
    let wide = Number(array[0]);
    let length = Number(array[1]);
    let totalPeaces = wide * length;
    let takenPeaces = 0;
    isNoPeaces = false;

    
    let index = 2;
    let command = (array[index]);
    index++;

    while (command !== "STOP") {
        let take = Number(command);
        takenPeaces += take;
        if (takenPeaces > totalPeaces) {
            isNoPeaces = true;
            break
        }
        
        command = array[index];
        index++;
    }
// if command is STOP, or  taken peaces > total
    let diff = Math.abs(totalPeaces - takenPeaces);

    if (isNoPeaces) {
        console.log(`No more cake left! You need ${diff} pieces more.`);
    } else {
        console.log(`${diff} pieces are left.`);
    }
    
    }
   
    vladi(["10",
    "10",
    "20",
    "20",
    "20",
    "20",
    "21"])
    ;
    vladi(["10",
    "2",
    "2",
    "4",
    "6",
    "STOP"])
    ;
