function vladi(input){

let depositSum = Number(input[0])
let durration = Number(input[1])
let yearlyPercent = Number(input[2])

yearlyPercent = yearlyPercent / 100
sum = depositSum + durration * ((depositSum * yearlyPercent) / 12)
console.log(sum)
    
    }
   
    vladi(["200 ","3 ","5.7 "]);