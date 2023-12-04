function vladi(array){

    let wide = Number(array[0]);
    let length = Number(array[1]);
    let height = Number(array[2]);
    let capacity = wide * length * height;
    let moved = 0;
    let isNoSpace = false;

    let index = 3;
    let command = array[index];
    index++;
    
    while (command !== "Done") {
        moved += Number(command);
        if (capacity <= moved) {
            isNoSpace = true;
            break;
        }
        command = array[index];
        index++;
    }
    // if command Done or capacity <= moved
    let diff = Math.abs(moved - capacity);
    
    if (isNoSpace) {
        console.log(`No more free space! You need ${diff} Cubic meters more.`);
    } else {
        console.log(`${diff} Cubic meters left.`);
    }
    
    }
   
    vladi(["10", 
    "10",
    "2",
    "20",
    "20",
    "20",
    "20",
    "122"])
    ;
    vladi(["10", 
    "1",
    "2",
    "4", 
    "6",
    "Done"])
    ;