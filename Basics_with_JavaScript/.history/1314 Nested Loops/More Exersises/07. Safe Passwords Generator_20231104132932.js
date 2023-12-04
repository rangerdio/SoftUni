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
    let xxStart = 1;
    let yyStart = 1;
	let isNoCombinations = false;

    
    while (maxGeneratedPwds > 0) {

        // for (let A1 = AA1; A1 < AA1 + 1; A1++ ) {
		// 	let A1Str = String.fromCharCode(A1);
		// 	passwordLine += A1Str;
			
		// 	if (AA1 > 55) {AA1 = 35;}
		// } //end of A1
        // AA1++;
		// for (let B1 = BB1; B1 < BB1 + 1; B1++ ) {
		// 	let B1Str = String.fromCharCode(B1);
		// 	passwordLine += B1Str;
		// 	if (BB1 > 96) {BB1 =64;}
		// //end of B1 
		// }
		// BB1++;

		for (let x = xxStart; x < xxStart + 1; x++ ) {
			console.log(``);
			for (let y = yyStart; y < yyStart + 1; y++ ) {
				passwordLine += "" + x + y;
				// if (xxStart === a && yyStart ===b) {isNoCombinations = true; break;}
				
				// if (xxStart == a + 1 || yyStart == b + 1) {break}
				console.log(x, y);
			//end of x  
			}
		
		//end of x  
		}
		xxStart++; yyStart++;
	
		// for (let B2 = BB2; B2 < BB2 + 1; B2++ ) {
		// 	let B2Str = String.fromCharCode(B2);
		// 	passwordLine += B2Str;
		// 	if (BB2 > 96) {BB2 =64;}
		// //end of B2  
		// }
		// BB2++;
		// for (let A2 = AA2; A2 < AA2 + 1; A2++ ) {
		// 	let A2Str = String.fromCharCode(A2);
		// 	passwordLine += A2Str + "|";
		// 	if (AA2 > 35) {AA2 = 55;}
		// //end of A2
		// }
		// AA2++;

    maxGeneratedPwds--;

	if (isNoCombinations) {break;}
    } // end of while

console.log(passwordLine);
}

vladi(["2","3","10"]);
// vladi(["20","50","10"]);
