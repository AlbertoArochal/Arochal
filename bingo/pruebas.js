const bingoCard = [];
let turnsCounter = 0;
let lineCounter = 0;
let playerName = "Player1";
let alreadyTaken = [];
const pastNumbers = [];
let nextNumber = 0;
let wins = 0;
const ranking = [
  {
    name: "Tucu",
    score: 1,
  },
  {
    name: "Frewasca",
    score: 50,
  },
];

const bingo = () => {
  PlayerName = prompt(
    "Welcome to ISDI Coders Bingo, dear user. What's your name?"
  );
  let instructions = confirm(
    `Dear ${PlayerName} , you have to complete your cardboard the less turns the better. You have 90 points now and you will lose 1 each turn. Do you want to want to play? `
  );
  if (instructions === true) {
    cardSelector();
    bingoTurn();
    console.log(`You completed the game in ${turnsCounter} turns`);
    showRanking();
  }
};

const cardGenerator = () => {
  let line = [];
  while (line.length < 5) {
    let cardNumber = Math.floor(Math.random() * (90 - 1 + 1)) + 1;

    if (!alreadyTaken.includes(cardNumber)) {
      line.push(cardNumber);
      alreadyTaken.push(cardNumber);
    }
    if (line.length === 5) {
      bingoCard.push(line);
      if (bingoCard.length === 3) {
        return;
      }
      cardGenerator();
    }
  }
};

const cardSelector = (choice) => {
  cardGenerator();
  choice = prompt(
    `Dear ${playerName}, here are your numbers ${bingoCard}. Do you want to keep this card and play?: y/n`
  );
  switch (choice) {
    case "y":
      console.log("lets play");
    case "n":
      bingoCard.pop();
      cardGenerator();
    default:
      cardSelector();
  }
};

const cardChecker = () => {
  for (i = 0; i < bingoCard.length; i++) {
    if (bingoCard[i].includes(nextNumber)) {
      alert("You have the winner number!");
      bingoCard[i][bingoCard[i].indexOf(nextNumber)] = "X";
      alert(`${bingoCard}`);
    }
  }
};

const bingoTurn = () => {
  jackpotNumber();
  cardChecker();
  lineChecker();
  bingoChecker();
  while (wins === 0) {
    let nextTurn = confirm("Do you want to play another turn?");
    if (nextTurn === true) {
      bingoTurn();
    } else {
      return;
    }
  }
};

const jackpotNumber = () => {
  nextNumber = Math.floor(Math.random() * (90 - 1 + 1)) + 1;
  switch (pastNumbers.includes(nextNumber)) {
    case true:
      jackpotNumber();
      break;
    case false:
      pastNumbers.push(nextNumber);
      console.log(pastNumbers);
      turnsCounter += 1;
      alert(`The new number is ${nextNumber}`);
  }
};

const lineChecker = () => {
  for (element of bingoCard) {
    if (element.every((value) => value === "X")) {
      if (lineCounter === 0) {
        alert("Linea!");
      }
      lineCounter += 1;
    }
  }
};

const bingoChecker = () => {
  if (
    bingoCard[0].every((value) => value === "X") &&
    bingoCard[1].every((value) => value === "X") &&
    bingoCard[2].every((value) => value === "X")
  ) {
    alert("***BINGO, YOU WON***");
    wins = +1;
    ranking.push({
      name: PlayerName,
      score: 91 - turnsCounter,
    });
  }
};

const showRanking = () => {
  let orderedRank = ranking.sort((a, b) => b.score - a.score);
  console.log(orderedRank);
};

bingo();
