function vladi(input){

    skumriaPrice = Number(input[0]);
    cacaPrice = Number(input[1]);
    kgPalamud = Number(input[2]);
    kgSafrid = Number(input[3]);
    kgMidi = Number(input[4]);
    
    palamudPrice = skumriaPrice * 1.6
    safridPrice = cacaPrice * 1.8
    midiPrice = 7.5

    bill = (palamudPrice * kgPalamud + safridPrice * kgSafrid + midiPrice * kgMidi).toFixed(2)
    console.log(bill);
    
    }
   
    vladi([6.90, 4.20, 1.5, 2.5, 1]);
    vladi([5.55, 3.57, 4.3, 3.6, 7]);
    vladi([7.79, 5.35, 9.3, 0, 0]);