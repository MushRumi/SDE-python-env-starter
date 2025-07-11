def countVowels(word):
    vowels = 'aeiouAEIOU'
    totalVowels = 0

    for letter in word:
        if letter in vowels:
            totalVowels += 1
    
    print(f"That word has {totalVowels} vowels!")

countVowels(input("Write down any word! I'll tell you how many vowels are in it: "))

#define countvowels with a word variable
# list out all the vowels in some way
# set the total vowel count at zero to begin with
# we wanna ask the user what word they want checked (this will be the word variable)
# some kinda for loop to check letters in the variable checked
# each time it finds that vowel it adds 1 to the total
#