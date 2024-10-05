function vladi(array) {
  let first = Number(array[0]);
  let second = Number(array[1]);
  let third = Number(array[2]);
  let combinationLine = "";

  for (let i = 1; i <= first; i++) {
    if (!(i % 2 === 0)) {
      continue;
    }

    for (let j = 2; j <= second; j++) {
      if (j === 4 || j === 6 || j === 8 || j === 9) {
        continue;
      }

      for (let k = 1; k <= third; k++) {
        if (!(k % 2 === 0)) {
          continue;
        }
        combinationLine = i + " " + j + " " + k;
        console.log(combinationLine);

        // end of third digit for loop / inner loop
      }

      // end of Second digit for loop / middle loop
    }

    // end of First Digit for loop / outer lop
  }
}

vladi(["3", "5", "5"]);
// vladi(["8", "2", "8"]);
