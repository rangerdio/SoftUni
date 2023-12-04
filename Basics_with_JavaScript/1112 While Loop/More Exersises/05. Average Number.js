function vladi(array) {
  let number = array[0];
  let top = 0;
  let sum = 0;

  let num = 0;
  num++;

  while (num <= number) {
    top = Number(array[num]);
    sum += top;
    num++;
  }
  let average = (sum / number).toFixed(2);
  console.log(average);
}

vladi(["4", "3", "2", "4", "2"]);
vladi(["2", "6", "4"]);
vladi(["3", "82", "43", "22"]);
vladi(["4", "95", "23", "76", "23"]);
