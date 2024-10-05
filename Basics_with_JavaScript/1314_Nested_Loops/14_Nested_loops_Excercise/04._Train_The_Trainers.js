function vladi(array) {
  let averageProject = 0;
  let averageFinal = 0;
  let counterTotal = 0;
  let juryQty = Number(array[0]);
  let index = 1;
  let command = array[index];
  index++;

  while (command !== "Finish") {
    let projectName = command;
    for (let i = 1; i <= juryQty; i++) {
      let grade = Number(array[index]);
      index++;
      averageProject += grade;
    }

    averageProject = averageProject / juryQty;
    console.log(`${projectName} - ${averageProject.toFixed(2)}.`);
    averageFinal += Number(averageProject);
    counterTotal += 1;
    averageProject = 0;

    command = array[index];
    index++;
  }
  averageFinal /= counterTotal;
  console.log(`Student's final assessment is ${averageFinal.toFixed(2)}.`);
}

vladi([
  "2",
  "While-Loop",
  "6.00",
  "5.50",
  "For-Loop",
  "5.84",
  "5.66",
  "Finish",
]);
vladi([
  "3",
  "Arrays",
  "4.53",
  "5.23",
  "5.00",
  "Lists",
  "5.83",
  "6.00",
  "5.42",
  "Finish",
]);
vladi([
  "2",
  "Objects and Classes",
  "5.77",
  "4.23",
  "Dictionaries",
  "4.62",
  "5.02",
  "RegEx",
  "2.88",
  "3.42",
  "Finish",
]);
