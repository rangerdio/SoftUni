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

    
    for (let A = AA1; A < AA1 + 2; A++ ) {
        let AStr = String.fromCharCode(A);
        passwordLine += AStr;
        AA1++;
        if (AA1 > 55) {AA1 =35;}
        } //end of A



    let B = 64;
    while (true) {
        if (B > 96) {B = 63;}
        let BStr = String.fromCharCode(B);


     passwordLine +=  BStr + "|"
        maxGeneratedPwds -= 1;
        if (maxGeneratedPwds === 0) {isMaxedPasswords = true; break;}
        
        B++;
        //end of B


        
    }
}

vladi(["2","3","10"]);
// vladi(["20","50","10"]);
