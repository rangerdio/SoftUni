function vladi(array){
    let isContinue = false;
    let letterCh = 0;
    let isCFound = false;
    let isOFound = false;
    let isNFound = false;
    let message = ""
    let word = ""
index = 0;
let letter = array[index];
index ++;

while (letter !== "End") {

    
    letterCh = letter.charCodeAt();
    let letterChLower = letter.toLowerCase();

    if (letterCh < 65 || letterCh > 122) {
        letter = array[index]; index ++; continue;
    } else if (letterCh > 90 && letterCh < 97) {
        letter = array[index]; index ++; continue;
    }

    if (isCFound && isOFound && isNFound === false && letter === "n") {
        message += word + " "; word = "";
        isCFound = false; isOFound = false; isNFound = false;
    } else if (isCFound && isNFound && !isOFound && letter === "o") {
        message += word + " "; word = "";
        isCFound = false; isOFound = false; isNFound = false;
    } else if (isNFound && isOFound && !isCFound && letter === "c") {
        message += word + " "; word = "";
        isCFound = false; isOFound = false; isNFound = false;
    } else if (isCFound && letter === "c") {word += letter;
    } else if (isOFound && letter === "o") {word += letter;
    } else if (isNFound && letter === "n") {word += letter;
    } else if (isCFound === false && letter === "c") {isCFound = true; letter = array[index]; index ++; continue;
    } else if (isOFound === false && letter === "o") {isOFound = true; letter = array[index]; index ++; continue;
    } else if (isNFound === false && letter === "n") {isNFound = true; letter = array[index]; index ++; continue;
    } else {word += letter;}

    letter = array[index];
    index ++;
    }

    console.log(message);


}


vladi(["H",
"n",
"e",
"l",
"l",
"o",
"o",
"c",
"t",
"c",
"h",
"o",
"e",
"r",
"e",
"n",
"e",
"End"]);
vladi(["%",
"!",
"c",
"^",
"B",
"`",
"o",
"%",
"o",
"o",
"M",
")",
"{",
"n",
"`\`",
"A",
"D",
"End"])

vladi(["o",
"S",
"%",
"o",
"l",
"^",
"v",
"e",
"c",
"n",
"&",
"m",
"e",
"c",
"o",
"n",
"End"]);
vladi();