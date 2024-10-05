function vladi(input){

let pencils = Number(input[0])
let markers = Number(input[1])
let fluid = Number(input[2])
let discount = Number(input[3])

pencilsPrice = 5.80
markersPrice = 7.20
fluidPrice = 1.2

moneyNeeded = (pencils * pencilsPrice + markers * markersPrice + fluid * fluidPrice) * (100 - discount) / 100

console.log(moneyNeeded)

    }
   
    vladi(["2 ","3 ","4 ","25 "]);