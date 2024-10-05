function vladi(array) {
  let startRange = Number(array[0]);
  let endRange = Number(array[1]);
  let luckyLine = "";

  for (let first = startRange; first <= endRange; first++) {
    let firstString = first + "";

    for (let second = startRange; second <= endRange; second++) {
      let secondString = second + "";

      for (let third = startRange; third <= endRange; third++) {
        let thirdString = third + "";

        for (let fourth = startRange; fourth <= endRange; fourth++) {
          let fourthString = fourth + "";

          if ((second + third) % 2 === 0 && first > fourth) {
            if (
              (first % 2 === 0 && fourth % 2 !== 0) ||
              (first % 2 !== 0 && fourth % 2 === 0)
            ) {
              luckyLine +=
                firstString + secondString + thirdString + fourthString + " ";
            }
          }
        }
      }
    }
  }
  console.log(luckyLine);
}

vladi(["2", "3"]);
vladi(["3", "5"]);
vladi(["5", "8"]);
