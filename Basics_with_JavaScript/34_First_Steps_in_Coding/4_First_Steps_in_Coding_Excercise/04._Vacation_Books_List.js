function vladi(input){

let pagesCurrentBook = Number(input[0])
let pagesPerHour = Number(input[1])
let daysToFinish = Number(input[2])
totalHoursNeeded = pagesCurrentBook / pagesPerHour
hoursToReadPerDay = totalHoursNeeded / daysToFinish
console.log(hoursToReadPerDay)

    }
   
    vladi(["212 ","20 ","2 "]);
