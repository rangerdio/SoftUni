function vladi(input) {
  let result = 0;

  for (let index = 0; index < input.length; index++) {
    let number = Number(input[index]);

    if (number >= 0) {
      console.log(`Result: ${(number * 2).toFixed(2)}`);
    } else {
      console.log(`Negative number!`);
    }
  }
}

vladi(["12", "43.2144", "12.3", "543.23", "-20"]);
vladi(["23.43", "12.3245", "0", "65.23432", "23", "65", "-12"]);
vladi(["-123"]);
