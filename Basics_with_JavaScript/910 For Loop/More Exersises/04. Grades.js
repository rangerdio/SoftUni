function vladi(array) {
  let studentsQty = Number(array[0]);
  let gradeSum = 0;
  let topQty = 0;
  let fourQty = 0;
  let threeQty = 0;
  let failQty = 0;
  let average = 0;

  for (let i = 1; i <= studentsQty; i++) {
    let grade = Number(array[i]);
    if (grade >= 5.0) {
      topQty += 1;
    } else if (grade >= 4.0 && grade <= 4.99) {
      fourQty += 1;
    } else if (grade >= 3.0 && grade <= 3.99) {
      threeQty += 1;
    } else if (grade < 3.0) {
      failQty += 1;
    }
    gradeSum += grade;
  }

  average = (gradeSum / studentsQty).toFixed(2);
  topQty = (topQty * 100 / studentsQty).toFixed(2);
  fourQty = (fourQty * 100 / studentsQty).toFixed(2);
  threeQty = (threeQty * 100 / studentsQty).toFixed(2);
  failQty = (failQty *100 / studentsQty).toFixed(2);
  console.log(`Top students: ${topQty}%`);
  console.log(`Between 4.00 and 4.99: ${fourQty}%`);
  console.log(`Between 3.00 and 3.99: ${threeQty}%`);
  console.log(`Fail: ${failQty}%`);
  console.log(`Average: ${average}`);
}

vladi([
  "10",
  "3.00",
  "2.99",
  "5.68",
  "3.01",
  "4",
  "4",
  "6.00",
  "4.50",
  "2.44",
  "5",
]);
vladi(["6", "2", "3", "4", "5", "6", "2.2"]);
