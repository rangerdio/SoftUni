function vladi(array) {
  let totalTicketCnt = 0;
  let studentPercent = 0;
  let standardPercent = 0;
  let kidPercent = 0;
  let studentCnt = 0;
  let standardCnt = 0;
  let kidCnt = 0;
  let studentCntTotal = 0;
  let standardCntTotal = 0;
  let kidCntTotal = 0;
  let moviePercent = 0;

  let index = 0;
  let movieName = array[index];
  index++;

  while (movieName !== "Finish") {
    let totalSeats = Number(array[index]);
    index++;
    let movieTickets = 0;
    let typeSeat = array[index];
    index++;

    while (typeSeat !== "End") {
      movieTickets += 1;

      switch (typeSeat) {
        case "student":
          studentCnt += 1;
          studentCntTotal += 1;
          break;
        case "standard":
          standardCnt += 1;
          standardCntTotal += 1;
          break;
        case "kid":
          kidCnt += 1;
          kidCntTotal += 1;
          break;
      }

      if (movieTickets === totalSeats) {
        break;
      }

      typeSeat = array[index];
      index++;

      // end of inside While loop
    }

    studentPercent = (100 * studentCnt) / movieTickets;
    standardPercent = (100 * standardCnt) / movieTickets;
    kidPercent = (100 * kidCnt) / movieTickets;
    totalTicketCnt += movieTickets;

    moviePercent = (100 * movieTickets) / totalSeats;
    console.log(`${movieName} - ${moviePercent.toFixed(2)}% full.`);

    studentCnt = 0;
    standardCnt = 0;
    kidCnt = 0;
    movieTickets = 0;

    movieName = array[index];
    index++;

    // end of outside While Loop
  }
  let studentTotalPercent = ((100 * studentCntTotal) / totalTicketCnt).toFixed(
    2
  );
  let standardTotalPercent = (
    (100 * standardCntTotal) /
    totalTicketCnt
  ).toFixed(2);
  let kidTotalPercent = ((100 * kidCntTotal) / totalTicketCnt).toFixed(2);

  console.log(`Total tickets: ${totalTicketCnt}`);
  console.log(`${studentTotalPercent}% student tickets.`);
  console.log(`${standardTotalPercent}% standard tickets.`);
  console.log(`${kidTotalPercent}% kids tickets.`);
}

vladi([
  "Taxi",
  "10",
  "standard",
  "kid",
  "student",
  "student",
  "standard",
  "standard",
  "End",
  "Scary Movie",
  "6",
  "student",
  "student",
  "student",
  "student",
  "student",
  "student",
  "Finish",
]);
vladi([
  "The Matrix",
  "20",
  "student",
  "standard",
  "kid",
  "kid",
  "student",
  "student",
  "standard",
  "student",
  "End",
  "The Green Mile",
  "17",
  "student",
  "standard",
  "standard",
  "student",
  "standard",
  "student",
  "End",
  "Amadeus",
  "3",
  "standard",
  "standard",
  "standard",
  "Finish",
]);
