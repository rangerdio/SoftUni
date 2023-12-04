function vladi(array){
	let ballQty = Number(array[0]);
    points = 0;
    let red = 0; let orange = 0; let yellow = 0; let white = 0; let black = 0; let out = 0;

    for (let i = 1; i <= ballQty; i++) {
        let color = array[i];
        
        switch (color) {
            case "red": points += 5; red += 1;  break;
            case "orange": points += 10; orange += 1;  break;
            case "yellow": points += 15; yellow += 1;  break;
            case "white": points += 20; white += 1;  break;
            case "black": points /= 2; points = Math.floor(points); black += 1;  break;
            default:
                out +=1;
                continue;
                break;

        }
    }

    console.log(`Total points: ${points}`)
    console.log(`Red balls: ${red}`)
    console.log(`Orange balls: ${orange}`)
    console.log(`Yellow balls: ${yellow}`)
    console.log(`White balls: ${white}`)
    console.log(`Other colors picked: ${out}`)
    console.log(`Divides from black balls: ${black}`)


    }
   
    vladi(["3",
    "white",
    "black",
    "pink"])
    ;
    vladi(["5",
    "red",
    "red",
    "ddd",
    "ddd",
    "ddd"])
    ;
