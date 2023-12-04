// function vladi(input) {
//   let number = Number(input[0]);
//   for (let num = 1; num <= 10; num++) {
//     console.log(`${num} * ${number} = ${num * number}`);
//   }
// }

// vladi(["5"]);

function vladi(input) {
  for (let index = 0; index < input.length; index++) {
    let number = Number(input[index]);

    for (let num = 1; num <= 10; num++) {
      console.log(`${num} * ${number} = ${num * number}`);
    }
  }
}
vladi(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]);
