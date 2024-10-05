function vladi(array) {
  let capacity = Number(array[0]);
  let visitorsCounter = 0;
  let incomeCurrent = 0;
  let income = 0;
  let isFull = false;
  let isMovieTime = false;

  let visitors = array[1];

  if (visitors === "Movie time!") {
    isMovieTime = true;
    pass;
  } else if (capacity - Number(visitors) < 0) {
    isFull = true;
  } else {
    visitors = Number(visitors);
    capacity -= visitors;
    visitorsCounter += visitors;
    // 3 bez ostatuk
    if (visitors % 3 === 0) {
      incomeCurrent = visitors * 5 - 5;
    } else {
      incomeCurrent = visitors * 5;
    }
    income += incomeCurrent;

    for (let i = 2; i < array.length; i++) {
      visitors = array[i];
      if (visitors === "Movie time!") {
        isMovieTime = true;
        break;
      }
      if (capacity - Number(visitors) < 0) {
        isFull = true;
        break;
      } else {
        visitors = Number(visitors);
        if (visitors % 3 === 0) {
          incomeCurrent = visitors * 5 - 5;
        } else {
          incomeCurrent = visitors * 5;
        }
        income += incomeCurrent;
        capacity -= visitors;
        visitorsCounter += visitors;
      }
    }
  }

  if (isMovieTime) {
    console.log(`There are ${capacity} seats left in the cinema.`);
  } else if (isFull) {
    console.log(`The cinema is full.`);
  }
  console.log(`Cinema income - ${income} lv.`);
}

vladi(["60", "10", "6", "3", "20", "15", "Movie time!"]);
vladi(["50", "15", "10", "10", "15", "5"]);
vladi([
  "100",
  "10",
  "10",
  "10",
  "10",
  "10",
  "10",
  "10",
  "10",
  "10",
  "10",
  "Movie time!",
]);
