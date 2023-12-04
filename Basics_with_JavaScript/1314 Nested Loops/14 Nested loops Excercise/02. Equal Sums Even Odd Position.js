function vladi(array) {
  let startNumber = Number(array[0]);
  let endNumber = Number(array[1]);
  let oddSum = 0;
  let evenSum = 0;
  let currentNum = 0;
  let currentNumString = "";
  let currentDigit = 0;
  let magicLine = "";

  for (let i = startNumber; i <= endNumber; i++) {
    currentNum = i;
    currentNumString = "" + currentNum;

    for (let j = 0; j < currentNumString.length; j++) {
      let currentDigitString = currentNumString.charAt(j);
      currentDigit = Number(currentDigitString);

      if (j % 2 === 0) {
        oddSum += currentDigit;
      } else {
        evenSum += currentDigit;
      }
    }

    if (oddSum == evenSum) {
      magicLine += currentNum + " ";
    }

    oddSum = 0;
    evenSum = 0;
  }
  console.log(magicLine);
}


vladi(["100000",
"100050"])
;
vladi(["123456",
"124000"])
;
vladi(["299900",
"300000"])
;
vladi(["100115",
"100120"])
;