function vladi(input) {
  let tabsOpened = Number(input[0]);
  let salary = Number(input[1]);
  flag = false;

  for (let index = 2; index < input.length; index++) {
    flag = false;
    let site = input[index];

    switch (site) {
      case "Facebook":
        salary -= 150;
        break;
      case "Instagram":
        salary -= 100;
        break;
      case "Reddit":
        salary -= 50;
        break;
    }
    if (salary <= 0) {
      break;
    } else {
      flag = true;
    }
  }
  if (flag) {
    console.log(Math.floor(salary));
  } else {
    console.log("You have lost your salary.");
  }
}

vladi([
  "10",
  "750",
  "Facebook",
  "Dev.bg",
  "Instagram",
  "Facebook",
  "Reddit",
  "Facebook",
  "Facebook",
]);
vladi(["3", "500", "Github.com", "Stackoverflow.com", "softuni.bg"]);
vladi(["3", "500", "Facebook", "Stackoverflow.com", "softuni.bg"]);
