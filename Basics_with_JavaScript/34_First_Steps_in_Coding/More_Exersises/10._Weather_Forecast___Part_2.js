function vladi(input){;

    let temp = Number(input[0]);

    if (temp >= 26 && temp <= 35) 
        {
        console.log("Hot");
        }
    else if (temp >= 20.1 && temp <= 25.9) 
        {
        console.log("Warm");
        }
    else if (temp >= 15.00 && temp <= 20.00) 
        {
        console.log("Mild");
        }
    else if (temp >= 12.00 && temp <= 14.9) 
        {
        console.log("Cool");
        }
    else if (temp >= 5.00 && temp <= 11.9) 
        {
        console.log("Cold");
        }
    else
        {
        console.log("unknown");
        }

    };
    vladi([16.5]);
    vladi([8]);
    vladi([22.4]);
    vladi([26]);
    vladi([0]);
