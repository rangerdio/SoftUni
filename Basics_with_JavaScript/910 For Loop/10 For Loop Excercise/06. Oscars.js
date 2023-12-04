function vladi(input) {
  let actorName = input[0];
  let academyPoints = Number(input[1]);
  let juryQty = Number(input[2]);
  let pointsSum = 0;
  let juryName = "";
  let juryPoints = 0;
  let juryNameLen = 0;
  let points = 0;
  let isNominated = false;
  let total = academyPoints;

  for (let index = 3; index < input.length; index++) {
    points = 0;
    if (index % 2 !== 0) {
      juryName = input[index];
      juryNameLen = juryName.length;
    } else {
      juryPoints = input[index];
      points = (juryPoints * juryNameLen) / 2;
      total += points;
      if (total > 1250.5) {
        isNominated = true;
        break;
      }
    } // heres the code should ends
  }
  total = total.toFixed(1);

  let diff = (1250.5 - total).toFixed(1);
  if (isNominated) {
    console.log(
      `Congratulations, ${actorName} got a nominee for leading role with ${total}!`
    );
  } else {
    console.log(`Sorry, ${actorName} you need ${diff} more!`);
  }
}

vladi([
  "Zahari Baharov",
  "205",
  "4",
  "Johnny Depp",
  "45",
  "Will Smith",
  "29",
  "Jet Lee",
  "10",
  "Matthew Mcconaughey",
  "39",
]);
vladi([
  "Sandra Bullock",
  "340",
  "5",
  "Robert De Niro",
  "50",
  "Julia Roberts",
  "40.5",
  "Daniel Day-Lewis",
  "39.4",
  "Nicolas Cage",
  "29.9",
  "Stoyanka Mutafova",
  "33",
]);
