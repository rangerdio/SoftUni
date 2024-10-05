function vladi(array) {
  let budged = Number(array[0]);
  let endYear = Number(array[1]);
  let startYear = 1800;
  let startAge = 18;
  let currAge = startAge - 1;
  let diff = 0;

  for (let year = startYear; year <= endYear; year++) {
    currAge += 1;
    if (year % 2 === 0) {
      budged -= 12000;
    } else {
      budged = budged - 12000 - 50 * currAge;
    }
  }
  diff = Math.abs(budged).toFixed(2);
  if (budged >= 0) {
    console.log(
      `Yes! He will live a carefree life and will have ${diff} dollars left.`
    );
  } else {
    console.log(`He will need ${diff} dollars to survive.`);
  }
}

vladi(["50000", "1802"]);
vladi(["10000.15", "1808"]);
