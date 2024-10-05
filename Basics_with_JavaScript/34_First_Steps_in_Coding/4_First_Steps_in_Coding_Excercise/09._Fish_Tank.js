function vladi(input){

    let lenght = Number(input[0])
    let wide = Number(input[1])
    let high = Number(input[2])
    let percent = Number(input[3])
    
    fullCapacity = (lenght * wide * high) / 1000
    leftCapacity = fullCapacity * (1 - 0.17)
    
    console.log(leftCapacity)
    
        }
       
        vladi(["85 ","75 ","47 ","17 "]);