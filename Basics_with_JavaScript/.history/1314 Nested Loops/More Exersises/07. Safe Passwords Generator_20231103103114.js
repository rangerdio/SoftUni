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

    
    for (let A1 = AA1; A1 < AA1 + 1; A1++ ) {
        let A1Str = String.fromCharCode(A1);
        passwordLine += A1Str;
        AA1++;
        if (AA1 > 55) {AA1 =35;}
    } //end of A1


    for (let B1 = BB1; B1 < BB1 + 1; B1++ ) {
        let B1Str = String.fromCharCode(B1);
        passwordLine += B1Str;
        BB1++;
        if (BB1 > 96) {BB1 =64;}
    //end of B1 
    }
    for (let x = xx; x < xx + 1; x++ ) {
        let xStr = String.fromCharCode(x);
        passwordLine += xStr;
        xx++;
        if (xx > maxGeneratedPwds) {break;}
    //end of x  
    }

    for (let y = yy; y < yy + 1; y++ ) {
        let yStr = String.fromCharCode(y);
        passwordLine += yStr;
        yy++;
        if (yy > maxGeneratedPwds) {break;}
    //end of x  
    }
    for (let B = BB1; B < BB1 + 1; B++ ) {
        let BStr = String.fromCharCode(B);
        passwordLine += BStr;
        BB1++;
        if (BB1 > 96) {BB1 =64;}
    //end of B  
    }





}

vladi(["2","3","10"]);
// vladi(["20","50","10"]);
