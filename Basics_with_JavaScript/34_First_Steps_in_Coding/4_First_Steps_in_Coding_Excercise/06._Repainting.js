function vladi(input){

let polyNeeded = Number(input[0])
let paintNeeded = Number(input[1])
let fluid = Number(input[2])
let hours = Number(input[3])

polyPrice = 1.50
paintPrice = 14.50
fluidPrice = 5.00

polyNeeded = polyNeeded + 2
paintNeeded = paintNeeded * 1.1
addsBads = 0.40
polySum = polyNeeded * polyPrice
paintSum = paintNeeded * paintPrice
fluidSum = fluid * fluidPrice
materials =  polySum + paintSum + fluidSum + addsBads
workersPricePerHour = materials * 0.3
total = materials + workersPricePerHour * hours

console.log(total)
    
    }
   
    vladi(["10 ","11 ","4 ","8 "]);