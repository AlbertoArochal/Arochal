const bingoCard = []
let turnsCounter = 0
let lineCounter = 1
const scoreBoard = {}

const cardGenerator = () => {
  let line = [];
  for (i = 0; i < 5; i++) {
    let cardNumber = Math.floor(Math.random() * (90 - 1 + 1)) + 1

    ;
    line.push(cardNumber);
    if (line.length === 5) {
      bingoCard.push(line);
      if (bingoCard.length === 3) {
        return
      }
      cardGenerator()
    }
  }
}

const cardSelector = (choice) => {
  choice =
    prompt(`Dear ${playerName}, here are your numbers ${bingoCard}. Do you want to keep this card and play?: y/n`);
  switch (choice) {
    case "y":
      placeholder;
    case "n":
      while (bingoCard.length > 0) {
        bingoCard.pop()
      };
      cardGenerator()
  }
}

const jackpotNumber = () => {
  let nextNumber = Math.floor(Math.random() * (90 - 1 + 1)) + 1;
  turnsCounter += 1;
  return nextNumber;
}

const numberChecker = () => {
  bingoCard.forEach(element =>
    if (element.includes(jackpotNumber)) {
      bingoCard[bingoCard.indexOf(jackpotNumber)] = "X";
      console.log(bingoCard)
    }
}

const lineChecker = () => {
  forEach(element =>
    if (element.every(valor => valor === "X")) {
      console.log("Linea!");
      lineCounter += 1
    })
}