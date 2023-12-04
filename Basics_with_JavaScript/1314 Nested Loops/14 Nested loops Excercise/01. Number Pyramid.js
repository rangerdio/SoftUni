function vladi(array) {
  let n = Number(array[0]);
  let counter = 0;
  isBigger = false;
  line = "";

  for (let row = 1; row <= n; row++) {
    for (let col = 1; col <= row; col++) {
      counter += 1;

      if (counter > n) {
        isBigger = true;
        break;
      }
      line += " " + counter;
    }

    console.log(line);
    line = "";

    if (isBigger) {
      break;
    }
  }
}
vladi(["7"]);
