function vladi(array) {
  let histogramQty = Number(array[0]);
  let p1 = 0; let p2 = 0; let p3 = 0; let p4 = 0; let p5 = 0;

  for (let index = 1; index < array.length; index++) {
    number = Number(array[index]);
    if (number < 200) {
      p1 += 1;
    } else if (number >= 200 && number < 400) {
      p2 += 1;
    } else if (number >= 400 && number < 600) {
      p3 += 1;
    } else if (number >= 600 && number < 800) {
      p4 += 1;
    } else if (number >= 800) {
      p5 += 1;
    }
  }

  console.log(`${((p1 / histogramQty) * 100).toFixed(2)}%`);
  console.log(`${((p2 / histogramQty) * 100).toFixed(2)}%`);
  console.log(`${((p3 / histogramQty) * 100).toFixed(2)}%`);
  console.log(`${((p4 / histogramQty) * 100).toFixed(2)}%`);
  console.log(`${((p5 / histogramQty) * 100).toFixed(2)}%`);
}

vladi(["3", "1", "2", "999"]);
vladi(["7", "800", "801", "250", "199", "399", "599", "799"]);
vladi(["9", "367", "99", "200", "799", "999", "333", "555", "111", "9"]);
vladi([
  "14",
  "53",
  "7",
  "56",
  "180",
  "450",
  "920",
  "12",
  "7",
  "150",
  "250",
  "680",
  "2",
  "600",
  "200",
]);
