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
	let isNoCombinations = false;

    
    while (maxGeneratedPwds > 0) {

        for (let A1 = AA1; A1 < AA1 + 1; A1++ ) {
			let A1Str = String.fromCharCode(A1);
			passwordLine += A1Str;
			
			if (AA1 > 55) {AA1 = 35;}
		} //end of A1
        AA1++;
		for (let B1 = BB1; B1 < BB1 + 1; B1++ ) {
			let B1Str = String.fromCharCode(B1);
			passwordLine += B1Str;
			if (BB1 > 96) {BB1 =64;}
		//end of B1 
		}
		BB1++;

		for (let x = xx; x < xx + 1; x++ ) {
			for (let y = yy; y < yy + 1; y++ ) {
				passwordLine += "" + x + y;
				if (xx === a && yy ===b) {isNoCombinations = true; break;}
				yy++;
				if xx == a + 1 || 1			//end of x  
			}
			if (isNoCombinations) {break;}
			
		//end of x  
		}
		xx++;
	
		for (let B2 = BB2; B2 < BB2 + 1; B2++ ) {
			let B2Str = String.fromCharCode(B2);
			passwordLine += B2Str;
			if (BB2 > 96) {BB2 =64;}
		//end of B2  
		}
		BB2++;
		for (let A2 = AA2; A2 < AA2 + 1; A2++ ) {
			let A2Str = String.fromCharCode(A2);
			passwordLine += A2Str + "|";
			if (AA2 > 35) {AA2 = 55;}
		//end of A2
		}
		AA2++;

    maxGeneratedPwds--;

	if (isNoCombinations) {break;}
    } // end of while

console.log(passwordLine);
}

vladi(["2","3","10"]);
// vladi(["20","50","10"]);
