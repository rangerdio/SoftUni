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
        let AStr = String.fromCharCode(A);
        passwordLine += AStr;
        AA1++;
        if (AA1 > 55) {AA1 =35;}
    } //end of A


    for (let B = BB1; B < BB1 + 1; B++ ) {
        let BStr = String.fromCharCode(B);
        passwordLine += BStr;
        BB1++;
        if (BB1 > 96) {BB1 =64;}
    //end of B  
    }
    for (let x = xx; x < xx + 1; x++ ) {
        let xStr = String.fromCharCode(B);
        passwordLine += xStr;
        xx++;
        if (xx > maxGeneratedPwds) {break;}
    //end of x  
    }

    for (let y = yy; y < yx + 1; y++ ) {
        let yStr = String.fromCharCode(B);
        passwordLine += yStr;
        yx++;
        if (yx > maxGeneratedPwds) {break;}
    //end of x  
    }



}

vladi(["2","3","10"]);
// vladi(["20","50","10"]);
