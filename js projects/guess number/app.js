const targetNumber = Math.floor(Math.random() * 100) + 1;

const input = document.getElementById("guessInput");
const submit = document.getElementById("submitGuess");
const message = document.getElementById("message");
const attempts = document.getElementById("attempts");

let guesses = 0;
const maxGuesses = 10;

attempts.innerText = guesses;

submit.addEventListener("click", () => {
  const guess = parseInt(input.value);
  input.value = "";

  validateGuess(guess);
});

function validateGuess(guess) {
  if (isNaN(guess) || guess < 1 || guess > 100) {
    message.innerText = "Please enter a number between 1 and 100!";
    return;
  }

  guesses++;
  attempts.innerText = guesses;

  checkGuess(guess);

  if (guesses >= maxGuesses && guess !== targetNumber) {
    message.innerText = `You lost! Random Number was ${targetNumber}`;
    input.disabled = true;
    submit.disabled = true;
  }
}

function checkGuess(guess) {
  if (guess < targetNumber) {
    message.innerText = "Number is too low!";
  } else if (guess > targetNumber) {
    message.innerText = "Number is too high!";
  } else {
    message.innerText = `You Won! Random Number was ${targetNumber}`;
    input.disabled = true;
    submit.disabled = true;
  }
}
