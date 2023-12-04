function vladi(array){

    let a = Number(array[0])
    let b = Number(array[1])
    let maxGeneratedPwds = Number(array[2])
    let passwordLine = ""

    let A = 35;
    while (true) {
        if (A > 55) { A = 35; }
        AStr = String.fromCharCode(A);

        
        let B = 64;
        while (true) {
            if (B > 96) { B = }
            
            B++;
            //end of B
        }


        // passwordLine += AStr + "|"
        // maxGeneratedPwds -= 1;
        // if (maxGeneratedPwds === 0) {break;}
        A++;
        //end of A
    }
    console.log(passwordLine);
}

vladi(["2","3","10"]);
vladi(["20","50","10"]);
