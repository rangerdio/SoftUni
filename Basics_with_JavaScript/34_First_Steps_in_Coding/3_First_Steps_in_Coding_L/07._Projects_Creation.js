function asd(input){

architectName = input[0]
projectQuantity = Number(input[1])
projectTime = 3
timeNeeded = projectQuantity * projectTime
console.log(`The architect ${architectName} will need ${timeNeeded} hours to complete ${projectQuantity} project/s.`)
}
asd(["George ","4 "]);
