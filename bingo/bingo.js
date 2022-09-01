let carton = [3, 34, 5, 25, 12]

const jackpotNumbers = () => {
    let nextNumber = Math.floor(Math.random() * (90 - 1 + 1)) + 1;
    return nextNumber
}

const match = () => {
    return carton.every(x => x === carton[0])
}

const bingoTurn = () => {
    let currNumber = carton.includes(jackpotNumbers());
    if (carton.includes(currNumber)) {
        carton[carton.indexOf(currNumber)] = "X";
        console.log(carton)
    }
    switch (carton.includes(jackpotNumbers())) {
        case true:
            return console.log("Bingo!");
        case false:
            turnChoice()
    }
}
/*const selectNumber = () => {
    for (let i = 0; i < 90; i++) {
        if (carton.includes(i)) {
            carton[carton.indexOf(i)] = "X"; console.log(carton); if (match() === true) {
                console.log("bingo!")
            }
        }
    }
}*/

/* const turnChoice = (choice) => {
    let choice = prompt("Do you want to try another turn? y/n");
    swich(true) {
        case "y": bingoTurn();
        case "n":
        default: turnChoice()
    }
} */

const turnChoice = (playerChoice) => {
    playerChoice = prompt("Do you want to play another turn? y/n"); 
    if (playerChoice === "y") {bingoTurn()}
    else if (playerChoice === "n") {return}
    else {turnChoice()}
    }



const bingo = (playerName) => {
    playerName =
        prompt("Hi dear customer, what's your name?");
    console.log(`Dear ${playerName}, here are your numbers ${carton}, let's play!`);
    bingoTurn();

}

bingo()