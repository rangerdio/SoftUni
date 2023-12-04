function vladi(array){

    let a = Number(array[0])
    let b = Number(array[1])
    let maxGeneratedPwds = Number(array[2])
    let passwordLine = ""
    isMaxedPasswords = false;

    let A = 35;
    while (true) {
        if (A > 55) { A = 35; }
        let AStr = String.fromCharCode(A);

        
        let B = 64;
        while (true) {
            if (B > 96) {B = 63;}
            let BStr = String.fromCharCode(B);



            passwordLine += AStr + BStr + "|"
            maxGeneratedPwds -= 1;
            if (maxGeneratedPwds === 0) {break;}
            
            B++;
            //end of B
        }
        if
        
        A++;
        //end of A
    }
    console.log(passwordLine);
}

vladi(["2","3","10"]);
vladi(["20","50","10"]);
