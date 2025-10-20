import { bold, blue, green, yellow, cyan, magenta, red } from "colorette";
import { readFileSync } from "fs";
import readline from "readline";

const data = JSON.parse(readFileSync("sentences.json", "utf8"));
const sentences = data.sentences;

// n random sentences
function getRandomSentences(n) {
  const shuffled = [...sentences].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, n);
}

const selected = getRandomSentences(5);

// intro message
console.log(bold(magenta("\n----------------- TYPING SPEED CLI -----------------")));
console.log(yellow(`\nType the following ${selected.length} sentences as fast and accurately as you can!\n`));

console.log(cyan(selected.join("\n")) + "\n");
console.log(green("\nPress ENTER to start..."));

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("", () => {
  console.log(cyan("\nStart typing below (press ENTER twice when done):\n"));
  startTyping();
});

function startTyping() {
  let lines = [];
  const start = Date.now();
  let lastLineEmpty = false;

  rl.on("line", (input) => {
    // Check for double enter (empty line after content)
    if (input.trim() === "" && lines.length > 0) {
      if (lastLineEmpty) {
        const end = Date.now();
        showResults(lines.join(" "), start, end);
        return;
      }
      lastLineEmpty = true;
    } else {
      lastLineEmpty = false;
      lines.push(input);
    }
  });
}

function showResults(typed, start, end) {
  const testText = selected.join(" ");
  const timeTaken = (end - start) / 1000;
  const words = typed.trim().split(/\s+/).filter(Boolean).length;
  const wpm = (words / timeTaken) * 60;

  const testWords = testText.split(/\s+/);
  const typedWords = typed.trim().split(/\s+/).filter(Boolean);
  
  let colored = "";
  let correct = 0;
  let totalChars = 0;

  for (let i = 0; i < Math.max(testWords.length, typedWords.length); i++) {
    const testWord = testWords[i] || "";
    const typedWord = typedWords[i] || "";
    
    if (i > 0) colored += " ";
    
    if (testWord === typedWord) {
      colored += green(typedWord);
      correct += typedWord.length;
      totalChars += testWord.length;
    } else {
      const maxLen = Math.max(testWord.length, typedWord.length);
      for (let j = 0; j < maxLen; j++) {
        if (j < testWord.length) totalChars++;
        
        if (j >= typedWord.length) {
          continue;
        } else if (j >= testWord.length) {
          colored += red(typedWord[j]);
        } else if (testWord[j] === typedWord[j]) {
          colored += green(typedWord[j]);
          correct++;
        } else {
          colored += red(typedWord[j]);
        }
      }
    }
  }

  const accuracy = totalChars > 0 ? (correct / totalChars) * 100 : 0;

  console.log(bold(magenta("\n----------------- RESULTS -----------------")));
  console.log(blue(`Time Taken: ${timeTaken.toFixed(2)} seconds`));
  console.log(blue(`Speed: ${wpm.toFixed(2)} words per minute`));
  console.log(blue(`Accuracy: ${accuracy.toFixed(2)}%`));

  console.log(bold(magenta("\nYour Typed Feedback:")));
  console.log(colored);
  
  console.log(bold(magenta("\nExpected Text:")));
  console.log(cyan(testText));

  console.log(bold(magenta("\n-------------------------------------------\n")));
  
  rl.close();
  process.exit(0);
}