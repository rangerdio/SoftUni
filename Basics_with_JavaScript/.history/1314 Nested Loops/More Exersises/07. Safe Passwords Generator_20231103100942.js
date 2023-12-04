function vladi(array){

    let a = Number(array[0])
    let b = Number(array[1])
    let maxGeneratedPwds = Number(array[2])
    let passwordLine = ""
    isMaxedPasswords = false;
    let AA1 = 35;
    let AA2 = 35;
    let BB1 = 64;
    let BB2 = 64;
    let xx = 1;
    let yy = 1;

    
    for (let A = AA1; A < AA1 + 1; A++ ) {
        if (A > 55) {A = AA1;}
        let AStr = String.fromCharCode(A);
        console.log``
        if (isMaxedPasswords) {break;}
        A++;
        
        } //end of A



    let B = 64;
    while (true) {
        if (B > 96) {B = 63;}
        let BStr = String.fromCharCode(B);


     passwordLine += AStr + BStr + "|"
        maxGeneratedPwds -= 1;
        if (maxGeneratedPwds === 0) {isMaxedPasswords = true; break;}
        
        B++;
        //end of B


        
    }
    console.log(passwordLine);
}

vladi(["2","3","10"]);
// vladi(["20","50","10"]);
