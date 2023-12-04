function vladi(array) {
  let manQty = Number(array[0]);
  let womenQty = Number(array[1]);
  let maxTables = Number(array[2]);
  let dateLine = "";
  let isNoFreeTables = false;

  for (let manNumber = 1; manNumber <= manQty; manNumber++) {
    let manNumberStr = manNumber + "";

    for (let womenNumber = 1; womenNumber <= womenQty; womenNumber++) {
      let womenNumberStr = womenNumber + "";
      maxTables--;
      dateLine += "(" + manNumberStr + " <-> " + womenNumberStr + ") ";
      if (maxTables === 0) {
        isNoFreeTables = true;
        break;
      }
      //inner loop End, Women
    }
    if (isNoFreeTables) {
      break;
      //outer Loop End , Man
    }
  }
  console.log(dateLine);
}

vladi(["2", "2", "6"]);
vladi(["2", "2", "3"]);
vladi(["5", "8", "40"]);
