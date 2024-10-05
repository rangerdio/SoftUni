function vladi(array) {
  let doubles = Number(array[0]);
  let currentPair = 0;
  let previousPair = 0;
  let maxDiff = 0;
  let savedMaxDiff = 0;
  let isEqual = true;

  for (let i = 1; i <= doubles * 2; i += 2) {
    previousPair = currentPair;
    let num1 = Number(array[i]);
    let num2 = Number(array[i + 1]);
    currentPair = num1 + num2;
    if (i === 1) {
      continue;
    }

    if (previousPair === currentPair) {
      continue;
    } else {
      maxDiff = Math.abs(previousPair - currentPair);
      isEqual = false;
    }

    if (maxDiff > savedMaxDiff) {
      savedMaxDiff = maxDiff;
    }
  }

  if (isEqual) {
    console.log(`Yes, value=${currentPair}`);
  } else {
    console.log(`No, maxdiff=${savedMaxDiff}`);
  }
}

vladi(["3", "1", "2", "0", "3", "4", "-1"]);
vladi(["4", "1", "1", "3", "1", "2", "2", "0", "0"]);
vladi(["2", "-1", "0", "0", "-1"]);
vladi(["2", "1", "2", "2", "2"]);
vladi(["1", "5", "5"]);
vladi(["2", "-1", "2", "0", "-1"]);
