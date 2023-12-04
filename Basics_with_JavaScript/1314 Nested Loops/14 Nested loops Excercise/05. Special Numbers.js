function vladi(array) {
  let number = Number(array[0]);
  let magicLine = "";

  for (let i = 1111; i <= 9999; i++) {
    let stringI = i + "";
    let stringLength = stringI.length;

    let isMagic = true;
    for (let j = 0; j < stringLength; j++) {
      let currentDigitString = stringI.charAt(j);
      let currentDigit = Number(currentDigitString);
      if (number % currentDigit !== 0) {
        isMagic = false;
      }

      // end of inside For loop
    }

    if (!isMagic) {
      isMagic = true;
      continue;
    } else {
      magicLine += stringI + " ";
    }

    // end of first For loop
  }

  console.log(magicLine);
}

vladi(["3"]);
vladi(["11"]);
vladi(["16"]);
