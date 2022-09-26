# Hangman

## Welcome

## Instructions
Hangman is a guessing game for two or more players. One player thinks of a word and the other(s) tries to guess it by suggesting letters within a certain number of guesses.

Logic: 
- The word to guess is represented by a row of dashes representing each letter of the word
- If the guessing player suggests a letter which occurs in the word, the other player writes it in all its correct positions
- If the suggested letter does not occur in the word, the other player draws one element of a hanged stick figure as a tally mark
- The player guessing the word may, at any time, attempt to guess the whole word
- If the word is correct, the game is over and the guesser wins
- Otherwise the other player may choose to penalise the guesser by adding an element to the diagram
- On the other hand, if the guesser makes enough incorrect guesses to allow the other player to complete the diagram, the guesser loses
- However, the guesser can also win by guessing all the letters that appear in the word, thereby completing the word, before the diagram is completed.

## Credits
[Hangman (game)](https://en.wikipedia.org/wiki/Hangman_(game)) helped a lot with the logic flow of the game