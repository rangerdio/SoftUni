function vladi(input){
    let toursPlayed = Number(input[0]);
    let startPoints = Number(input[1]);
    let result = "";
    let tourPoints = 0;
    let finalPoints = startPoints;
    let winCount = 0;
    let averagePoints = 0;
    let winPercentage = 0;

    for (let index = 2; index < input.length; index++) {
        result = input[index];
        
        switch (result) {
            case "W":
                tourPoints = 2000;
                winCount += 1;
                break;
            case "F":
                tourPoints = 1200;
                break;
            case "SF":
                tourPoints = 720;
                break;
        }
        finalPoints += tourPoints;
    }

    averagePoints = Math.floor((finalPoints - startPoints) / toursPlayed);
    winPercentage = (100 * winCount / toursPlayed).toFixed(2);
    console.log(`Final points: ${finalPoints}`);
    console.log(`Average points: ${averagePoints}`)
    console.log(`${winPercentage}%`)
    }
   
    vladi(["5",
"1400",
"F",
"SF",
"W",
"W",
"SF"])
;
    vladi(["4",
"750",
"SF",
"W",
"SF",
"W"])
;
    vladi(["7",
"1200",
"SF",
"F",
"W",
"F",
"W",
"SF",
"W"])
;