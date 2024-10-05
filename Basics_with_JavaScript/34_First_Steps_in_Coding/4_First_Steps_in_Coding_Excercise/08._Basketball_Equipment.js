function vladi(array){

    let yearTax = Number(array[0])
    
    shoes = yearTax * 0.6
    shirts = shoes * 0.8
    ball = shirts / 4
    accesoaries = ball / 5
    totalCosts = yearTax + shoes + shirts + ball + accesoaries
    
    console.log(totalCosts)
        
        }
       
        vladi([320]);