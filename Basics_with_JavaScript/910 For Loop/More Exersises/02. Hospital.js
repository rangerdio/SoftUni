function vladi(array) {
  let days = Number(array[0]);
  let doctors = 7;
  let treated = 0;
  let notTreated = 0;
  let totalTreated = 0;
  let totalNotTreated = 0;
  let patients = 0;
  let day = 0;

  for (let day = 1; day <= days; day++) {
    if (day % 3 === 0 && notTreated > treated) {
      doctors += 1;
      notTreated = 0;
      treated = 0;
    } else if (day % 3 === 0 && notTreated < treated) {
      notTreated = 0;
      treated = 0;
    }

    patients = Number(array[day]);

    if (doctors >= patients) {
      treated += patients;
      totalTreated += patients;
      notTreated += 0;
      totalNotTreated += 0;
    } else {
      treated += doctors;
      totalTreated += doctors;
      notTreated += patients - doctors;
      totalNotTreated += patients - doctors;
    }
  }

  console.log(`Treated patients: ${totalTreated}.`);
  console.log(`Untreated patients: ${totalNotTreated}.`);
}

vladi(["4", "7", "27", "9", "1"]);
vladi(["6", "25", "25", "25", "25", "25", "2"]);
vladi(["3", "7", "7", "7"]);
