function vladi(input){

let chikenMenuQuantity = Number(input[0])
let fishMenuQuantity = Number(input[1])
let vegetarianMenuQuantity = Number(input[2])

chickenMenuPrice = 10.35
fishMenuPrice = 12.40
vegeterianMenuPrice = 8.15

bill = (chikenMenuQuantity * chickenMenuPrice + fishMenuQuantity * fishMenuPrice + vegetarianMenuQuantity * vegeterianMenuPrice) * 1.2 + 2.50

console.log(bill)

    }
   
    vladi(["2 ","4 ","3 "]);