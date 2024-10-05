function vladi(input) {
  let groups = Number(input[0]);
  let musalaQty = 0;
  let monblanQty = 0;
  let kilimQty = 0;
  let everestQty = 0;
  let k2Qty = 0;
  let counter = 0;

  for (let index = 1; index < input.length; index++) {
    peopleInGroup = Number(input[index]);

    if (peopleInGroup <= 5) {
      musalaQty += peopleInGroup;
      counter += peopleInGroup;
    } else if (peopleInGroup > 5 && peopleInGroup <= 12) {
      monblanQty += peopleInGroup;
      counter += peopleInGroup;
    } else if (peopleInGroup > 12 && peopleInGroup <= 25) {
      kilimQty += peopleInGroup;
      counter += peopleInGroup;
    } else if (peopleInGroup > 25 && peopleInGroup <= 40) {
      k2Qty += peopleInGroup;
      counter += peopleInGroup;
    } else if (peopleInGroup > 40) {
      everestQty += peopleInGroup;
      counter += peopleInGroup;
    }
  }
  let musala = (100 * musalaQty / counter).toFixed(2);
  let monblan = (100 * monblanQty / counter).toFixed(2);
  let kili = (100 * kilimQty / counter).toFixed(2);
  let k2 = (100 * k2Qty / counter).toFixed(2);
  let everest = (100 * everestQty / counter).toFixed(2);
  console.log(`${musala}%`);
  console.log(`${monblan}%`);
  console.log(`${kili}%`);
  console.log(`${k2}%`);
  console.log(`${everest}%`);
}

vladi(["10", "10", "5", "1", "100", "12", "26", "17", "37", "40", "78"]);
vladi(["5", "25", "41", "31", "250", "6"]);
