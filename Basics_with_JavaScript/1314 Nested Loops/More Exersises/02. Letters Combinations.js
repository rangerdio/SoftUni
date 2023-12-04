function vladi(array) {
  let startNum = array[0];
  let endNum = array[1];
  let badLetter = array[2];
  let counter = 0;
  let combinationLine = "";

  let startNumDigit = startNum.charCodeAt(0);
  let endNumDigit = endNum.charCodeAt(0);
  let badLetterDigit = badLetter.charCodeAt(0);

  for (let first = startNumDigit; first <= endNumDigit; first++) {
    let firstString = String.fromCharCode(first);
    if (first === badLetterDigit) {
      continue;
    }

    for (let second = startNumDigit; second <= endNumDigit; second++) {
      let secondString = String.fromCharCode(second);
      if (second === badLetterDigit) {
        continue;
      }
      for (let third = startNumDigit; third <= endNumDigit; third++) {
        let thirdString = String.fromCharCode(third);
        if (third === badLetterDigit) {
          continue;
        }
        //counter to be moved after all successful rules
        counter++;
        combinationLine += firstString + secondString + thirdString + " ";

        // end of inner loop
      }

      // end of middle loop
    }

    // end of outer loop
  }
  combinationLine = combinationLine + counter;
  console.log(combinationLine);
}

vladi(["a", "c", "b"]);
vladi(["f", "k", "h"]);
vladi(["a", "c", "z"]);
