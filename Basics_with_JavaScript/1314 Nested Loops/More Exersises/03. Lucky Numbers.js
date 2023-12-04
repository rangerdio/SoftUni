function vladi(array) {
  let luckyLine = "";
  let n = Number(array[0]);

  for (let first = 1; first <= 9; first++) {
    let firstString = first + "";

    for (let second = 1; second <= 9; second++) {
      let secondString = second + "";

      for (let third = 1; third <= 9; third++) {
        let thirdString = third + "";

        for (let fourth = 1; fourth <= 9; fourth++) {
          let fourthString = fourth + "";

          if (first + second === third + fourth && n % (first + second) === 0) {
            luckyLine +=
              firstString + secondString + thirdString + fourthString + " ";
          }
          //end of inner top Loop
        }
        //end of inner right Loop
      }
      //end of inner left Loop
    }
    //end of outer Loop
  }
  console.log(luckyLine);
}

vladi(["3"]);
vladi(["7"]);
vladi(["24"]);
