#access libraries and py files 
import functions as f
import os
import time

def clearScreen():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
#Initialize variables and setup 
#Need to keep track of correct letters, incorrect letters and tries



#Make a list of the spider drawings



#Print intro statements (welcome to game, etc)



#generate a random word from word list





secretWord = f.generate_word()
incorrectGuesses = []
correctGuesses = []
numberOfIncorrectGuesses = 0

gameOver = False

while not gameOver:
  #get input from user
  f.introduction()
  f.print_word(secretWord, correctGuesses)
  numberOfIncorrectGuesses = f.check_word(correctGuesses, incorrectGuesses, secretWord, numberOfTries)
  time.sleep(3)
  clearScreen()
  #spider gets printed
  f.print_spider(numberOfIncorrectGuesses)

  #check for LOSE or WIN
  if numberOfIncorrectGuesses < 6:
    print("You lost!")
    gameOver = True
    pass

  if all(letter in correctGuesses for letter in set(secretWord)):
    print("You win!")
    gameOver = True
    pass

  wonGame = True
  for letter in secretWord:
    if (letter not in correctGuesses):
      wonGame = False
      break
  
  if wonGame:
    print("You win!")
    gameOver = True


# game loop
f.introduction()
playAgain = True
while playAgain:
  os.system("cls")
  playGame()

  userChoice = input("Would you like to play again? ").lower()
  playAgain = userChoice.lower() == "yes"

