function vladi(array) {
  primeSum = 0;
  nonPrimeSum = 0;
  let i = 0;
  let command = array[i];
  i++;

  while (command !== "stop") {
    let currentNumber = Number(command);
    let isPrime = true;

    if (currentNumber < 0) {
      console.log(`Number is negative.`);
    } else if (currentNumber === 1) {
      isPrime = false;
    } else {
      for (let j = 2; j <= currentNumber - 1; j++) {
        if (currentNumber % j === 0) {
          isPrime = false;
          break;
        }
      }
    }

    if (isPrime && currentNumber > 0) {
      primeSum += currentNumber;
    } else if (!isPrime && currentNumber > 0) {
      nonPrimeSum += currentNumber;
    }

    command = array[i];
    i++;
  }

  console.log(`Sum of all prime numbers is: ${primeSum}`);
  console.log(`Sum of all non prime numbers is: ${nonPrimeSum}`);
}

vladi(["3", "9", "0", "7", "19", "4", "stop"]);
vladi(["30", "83", "33", "-1", "20", "stop"]);
vladi(["0", "-9", "0", "stop"]);
