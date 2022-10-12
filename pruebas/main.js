const questions = [
    {letter: "a", answer: "abducir", status: 0, question: ("CON LA A. Dicho de una supuesta criatura extraterrestre: Apoderarse de alguien")},
	{letter: "b", answer: "bingo", status: 0, question: ("CON LA B. Juego que ha sacado de quicio a todos los 'Skylabers' en las sesiones de precurso")},
	{letter: "c", answer: "churumbel", status: 0, question: ("CON LA C. Niño, crío, bebé")},
	{letter: "d", answer: "diarrea", status: 0, question: ("CON LA D. Anormalidad en la función del aparato digestivo caracterizada por frecuentes evacuaciones y su consistencia líquida")},
	{letter: "e", answer: "ectoplasma", status: 0, question: ("CON LA E. Gelatinoso y se encuentra debajo de la membrana plasmática. Los cazafantasmas medían su radiación")},
	{letter: "f", answer: "facil", status: 0, question: ("CON LA F. Que no requiere gran esfuerzo, capacidad o dificultad")},
	{letter: "g", answer: "galaxia", status: 0, question: ("CON LA G. Conjunto enorme de estrellas, polvo interestelar, gases y partículas")},
	{letter: "h", answer: "harakiri", status: 0, question: ("CON LA H. Suicidio ritual japonés por desentrañamiento")},
	{letter: "i", answer: "iglesia", status: 0, question: ("CON LA I. Templo cristiano")},
	{letter: "j", answer: "jabali", status: 0, question: ("CON LA J. Variedad salvaje del cerdo que sale en la película 'El Rey León', de nombre Pumba")},
	{letter: "k", answer: "kamikaze", status: 0, question: ("CON LA K. Persona que se juega la vida realizando una acción temeraria")},
	{letter: "l", answer: "licantropo", status: 0, question: ("CON LA L. Hombre lobo")},
	{letter: "m", answer: "misantropo", status: 0, question: ("CON LA M. Persona que huye del trato con otras personas o siente gran aversión hacia ellas")},
	{letter: "n", answer: "necedad", status: 0, question: ("CON LA N. Demostración de poca inteligencia")},
	{letter: "ñ", answer: "señal", status: 0, question: ("CONTIENE LA Ñ. Indicio que permite deducir algo de lo que no se tiene un conocimiento directo.")},
	{letter: "o", answer: "orco", status: 0, question: ("CON LA O. Humanoide fantástico de apariencia terrible y bestial, piel de color verde creada por el escritor Tolkien")},
	{letter: "p", answer: "protoss", status: 0, question: ("CON LA P. Raza ancestral tecnológicamente avanzada que se caracteriza por sus grandes poderes psíonicos del videojuego StarCraft")},
	{letter: "q", answer: "queso", status: 0, question: ("CON LA Q. Producto obtenido por la maduración de la cuajada de la leche")},
	{letter: "r", answer: "raton", status: 0, question: ("CON LA R. Roedor")},
	{letter: "s", answer: "stackoverflow", status: 0, question: ("CON LA S. Comunidad salvadora de todo desarrollador informático")},
	{letter: "t", answer: "terminator", status: 0, question: ("CON LA T. Película del director James Cameron que consolidó a Arnold Schwarzenegger como actor en 1984")},
	{letter: "u", answer: "unamuno", status: 0, question: ("CON LA U. Escritor y filósofo español de la generación del 98 autor del libro 'Niebla' en 1914")},
	{letter: "v", answer: "vikingos", status: 0, question: ("CON LA V. Nombre dado a los miembros de los pueblos nórdicos originarios de Escandinavia, famosos por sus incursiones y pillajes en Europa")},
	{letter: "w", answer: "sandwich", status: 0, question: ("CONTIENE LA W. Emparedado hecho con dos rebanadas de pan entre las cuales se coloca jamón y queso")},
	{letter: "x", answer: "botox", status: 0, question: ("CONTIENE LA X. Toxina bacteriana utilizada en cirujía estética")},
	{letter: "y", answer: "peyote", status: 0, question: ("CONTIENE LA Y. Pequeño cáctus conocido por sus alcaloides psicoactivos utilizado de forma ritual y medicinal por indígenas americanos")},
	{letter: "z", answer: "zen", status: 0, question: ("CON LA Z. Escuela de budismo que busca la experiencia de la sabiduría más allá del discurso racional")},
]

let count = 0

class UserConstructor {
    Name;
    score;
    constructor(id, Name, score) {
        this.score = {
            successes: 0,
            failures: 0
        }
        this.Name
        this.description = function () {
            rankingPlayerFooter.textContent = ("Player name: " + this.Name + ", Correct answers: " + this.score.successes + " Incorrect answers: " + this.score.failures)
        }
    }
}

const user = new UserConstructor()

const finish = () => {
    user.description()
    document.getElementById('question').textContent = "You have finished the game!"
    document.getElementById('Text').style.display = 'none'
    startGameOrSend.style.display = 'none'
    pasapalabra.textContent = "Play again?"  
}

const showMessage = () => {
    document.getElementById("message").style.display = "block"
    function hideSpan () {
        document.getElementById("message").style.display = "none"
    }
    setTimeout(hideSpan, 2000)
} 

const checkAnswer = (playerAnswer = "", question) => {
    if(playerAnswer !== question.answer){
        document.getElementById(count).style.backgroundColor = "red"
        document.getElementById('message').textContent = "Failure"
        showMessage()
        question.status = -1
        user.score.failures ++
        return
    }
    document.getElementById(count).style.backgroundColor = "green"
    document.getElementById('message').textContent = "Correct"
    showMessage()
    question.status = 1
    user.score.successes ++
    return 
}

const rankingPlayerFooter = document.getElementById('score')
const startGameOrSend = document.querySelector('[data-startOrSend]')
const pasapalabra = document.querySelector('[data-pasapalabra]')
const answer = document.getElementById('answer')
const letters = document.querySelectorAll('[data-letters]')
const inputText = document.getElementById('inputText')

const resetGame = () => {
    count = 0
    user.score.failures = 0
    user.score.successes = 0
    rankingPlayerFooter.textContent = ''
    letters.forEach(element => element.style.backgroundColor = '#2e9de7')
    questions.forEach(element => element.status = 0)
    console.table(questions)
    inputText.textContent = "What's your name?"
    startGameOrSend.textContent = 'START'
    startGameOrSend.style.display = 'inline'
    pasapalabra.textContent = "PASAPALABRA"
    document.getElementById('question').textContent = ''
    //player.pop()
}
const clearAnswer = () => {
    answer.value = ''
}
const updateDisplayQuestion = () => {
    if(questions.every((element) => element.status !== 0)){
        finish()
        return
    }
    if(questions[count].status !== 0){
        count ++
        updateDisplayQuestion()
    }
    document.getElementById('question').textContent = questions[count].question
}
const resetRound = () => {
    count = -1
}

startGameOrSend.addEventListener('click', button => {
    let buttonValue = startGameOrSend.innerText
    switch (buttonValue) {
        case 'START':
        startGameOrSend.textContent = 'SEND';
        document.getElementById('Text').style.display = 'block'
        return
        case 'SEND':
        user.Name = answer.value
        updateDisplayQuestion()
        startGameOrSend.textContent = 'ENTER';    
        inputText.textContent = 'Answer'
        clearAnswer()
        return
    }
    checkAnswer(answer.value.toLowerCase(), questions[count])
    if(count > 25){
        resetRound()
    }
    clearAnswer()
    count ++
    updateDisplayQuestion()
})

pasapalabra.addEventListener('click', button => {
    if(pasapalabra.innerText == 'Play again?'){
        resetGame()
        return
    }
    if(count > 25){
        resetRound()
    }
    clearAnswer()
    count ++
    updateDisplayQuestion()
})