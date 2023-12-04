function vladi(input) {
  let nonWorkDays = Number(input);
  let workingDays = 365 - nonWorkDays;
  let tomNeeds = 30000;
  let totalNonWorkDayPlay = nonWorkDays * 127;
  let totalWorkDayPlay = workingDays * 63;
  let totalPlay = totalNonWorkDayPlay + totalWorkDayPlay;
  let difference = Math.abs(totalPlay - tomNeeds);
  let H = Math.floor(difference / 60);
  let M = difference % 60;
  if (totalPlay > tomNeeds) {
    console.log(`Tom will run away`);
    console.log(`${H} hours and ${M} minutes more for play`);
  } else {
    console.log(`Tom sleeps well`);
    console.log(`${H} hours and ${M} minutes less for play`);
  }
}

vladi([20]);
vladi([113]);
