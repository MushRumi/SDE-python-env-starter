import spiderDraw as sd
import random



# Prompts user for letter guess. Checks through the secret word to see if it contains the letter guessed by the user. Returns the number of wrong guesses
#Takes in the correct letter list, incorrect letter list, secret word and the number of tries as parameters.
def check_word(correctLetterList, incorrectLetterList, secretWord, numberOfTries):
  validGuess = False
  userGuess = ""
  while not validGuess:
    userGuess = input("Please guess a letter. ")
    if len(userGuess) > 1 or len(userGuess) == 0:
      print("Please guess only a single letter. ")
      continue
    if not userGuess.isalpha():
      print("Please only guess a letter, no symbols. ")
      continue
    if userGuess in correctLetterList or userGuess in (incorrectLetterList):
      print(f"You have already guessed the letter {userGuess}, please choose another letter.")

    validGuess = True

    if userGuess in secretWord:
      print(f"The letter {userGuess} is in the word!")
      correctLetterList.append(userGuess)
      return numberOfTries
    else:
      print(f"The letter {userGuess} is not in the word :(")
      incorrectLetterList.append(userGuess)
      return numberOfTries + 1

  pass
  





# Returns the word to the console containing "_" for any letter not guessed by the user.
#Takes in the correct word and the list of correct guesses as parameters
def print_word(mysteryWord):
    display = ""
    for letter in secretWord:
      display += letter + " "
    else:
      dispaly += "_ "
    print(display.strip())

    pass



# Prints spider from the spider drawing functions in the spiderDraw.py file. Takes the number of wrong guesses and the list of spider drawing functions as parameters.

def print_spider(numIncorrectGuess):
    sd.listOfSpiders[numIncorrectGuess]()

    pass
  
    



#Opens the word list text file, stores the contents into a list, chooses a random word from the list, finds the length of that word and prints a string of blanks for each letter in the word. Returns the word.
def generate_word():
  wordlist = open("words.txt").read().split()
  word = random.choice(wordlist) #Choose a random word from the list
  return word


  

#Put the introduction code/input player name into here 
def introduction():
    name = input("What is your name? ")
    print(f'Hello, {name}!')
    pass

generate_word()
pass