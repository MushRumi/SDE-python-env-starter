name = input('What is your name? ')
print(f'Welcome to your escape room, {name}!')
print('')

#first room (choosing 1 of 3 doors)
def room1():
    print('You are met with three doors labeled 1, 2, and 3.')
    guess = int(input('Which door will you open to continue? '))

    if guess == 1:
        print('You walk through the door into the next room.')
    elif guess == 2:
        print('')
        print('You walk through the door into a teleportation trap! You are back at where you started!')
        print('')
        room1()
    elif guess == 3:
        print('')
        print('You fall into a pit... Better luck next time.')
        print('')
    else:
        print('')
        print('Not a valid choice! Your choices are 1, 2, and 3.')
        print('')
        room1()

#start the thingy, basically calling main or whatever
room1()