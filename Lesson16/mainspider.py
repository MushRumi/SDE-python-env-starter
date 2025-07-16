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




#Game Loop
secretWord = f.generate_word()
incorrectGuesses = []
corrtectGuesses = []
numberOfIncorrectGuesses = []

while True:
  #get input from user
  f.print_word(secretWord, correctGuesses)
  numberOfIncorrectGuesses = f.check_word(correctGuesses, incorrectGuesses, secretWord, numberOfTries)
  time.sleep(3)
  clearScreen()
  f.print_spider(numberOfIncorrectGuesses)

  #This is where you'll call all of your functions. Just need to decide the proper order.


  #You will also need to specify your win and lose conditions in here