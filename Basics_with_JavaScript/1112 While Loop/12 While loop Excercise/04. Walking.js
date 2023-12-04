function vladi(array){
    let goal = 10000;
    let walked_steps = 0;
    let steps = 0
    let index = 0;
    let isGoalReached = false;
    let isGoingHome = false;
    let command = array[index];
    index++;

    while (true) {
        if (command === "Going home") {
            isGoingHome = true;
            command = Number(array[index]);
            walked_steps += command;
            if (walked_steps >= goal) {
                isGoalReached = true;
            }
            break;
        }
        
        steps = Number(command);
        walked_steps += steps;
        if (walked_steps >= goal) {
            isGoalReached = true;
            break;
        }
        command = array[index];
        index++;
    }

    let diff = Math.abs(goal - walked_steps)
    if (isGoalReached) {
        console.log(`Goal reached! Good job!`)
        console.log(`${diff} steps over the goal!`);
    } else {
        console.log(`${diff} more steps to reach goal.`);
    }
    }
   
    vladi(["1000",
    "1500",
    "2000",
    "6500"])
    ;
    vladi(["1500",
    "3000",
    "250",
    "1548",
    "2000",
    "Going home",
    "2000"])
    ;
    vladi(["1500",
    "300",
    "2500",
    "3000",
    "Going home",
    "200"])
    ;
    vladi(["125",
    "250",
    "4000",
    "30",
    "2678",
    "4682"])
    ;