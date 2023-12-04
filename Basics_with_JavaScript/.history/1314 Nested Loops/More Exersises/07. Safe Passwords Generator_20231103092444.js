function vladi(array){

    let a = Number(array[0])
    let b = Number(array[1])
    let maxGeneratedPwds = Number(array[2])
    let passwordLine = ""

    let first = 34;
    first++;

    while (true) {
        if (first > 55) { first = 35; }
        firstStr = String.fromCharCode(0);



        passwordLine += +|
        maxGeneratedPwds -= 1;
        if (maxGeneratedPwds === 0) {break;}
        first++;
        //end of first
    }
    console.log(passwordLine);
}

vladi(["2","3","10"]);
vladi(["20","50","10"]);
