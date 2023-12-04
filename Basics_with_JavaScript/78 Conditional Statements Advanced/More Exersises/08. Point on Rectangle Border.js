function vladi(input) {
  let x1 = Number(input[0]);
  let y1 = Number(input[1]);
  let x2 = Number(input[2]);
  let y2 = Number(input[3]);
  let x = Number(input[4]);
  let y = Number(input[5]);
  isBorder = false;

  if (x === x1 || x === x2) {
    if (y >= y1 && y <= y2) {
      isBorder = true;
    } else {
      isBorder = false;
    }
  } else if (y === y1 || y === y2) {
    if (x >= x1 && x <= x2) {
      isBorder = true;
    } else {
      isBorder = false;
    }
  } else {
    isBorder = false;
  }

  if (isBorder) {
    console.log("Border");
  } else {
    console.log("Inside / Outside");
  }
}

vladi(["2", "-3", "12", "3", "8", "-1"]);
vladi(["2", "-3", "12", "3", "12", "-1"]);
