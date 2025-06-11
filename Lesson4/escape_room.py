import random
name = input('What is your name? ')
print(f'Welcome to your dungeon escape room, {name}!')
print('')

#first room (choosing 1 of 3 doors)
def room1():
    print('You are met with three runic doors labeled 1, 2, and 3.')
    guess = int(input('Which door will you open to continue? '))

    if guess == 1:
        print('You walk through the door into the next room.')
        print('')
        print('You find moving glyphs of an ancient language on the walls, and a keypad in the middle of the room.')
        print('')
        room2(4)
    elif guess == 2:
        print('')
        print('You walk through the door into a sleeping gas trap! You are back at where you started!')
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

def room2(timer):
    #give answer choices
    possiblepasswords = ['alpha', 'jerky', 'semi', 'evan', 'tracker']
    correctpassword = random.choice(possiblepasswords)
    print('Make your guess.')
    for password in possiblepasswords:
        if password == correctpassword:
            print(password.upper())
        else:
            print(password)
    
    #guessing and time tracking; a path splits here
    guess2 = input()
    if guess2 == correctpassword:
        print('')
        print('The roof opens and a rope falls down as the floor sinks around you.')
        if timer >= 2:
            print('You feel a breeze of sharp wind whiff by your ankle as you climb out.')
            #room2a()
        else:
            print('Something beastly has grabbed you by the legs.')
            print('You are dragged down into the depths. Too slow.')
            #room2b()
    else:
        timer -= 1
        print('The ground shakes. You get the feeling you are not meant to be here.')
        print('You must hurry.')
        print('')
        if timer > 0:
            room2(timer)
        else:
            print('You overstayed your welcome and fall into the depths.')
            #room2b()


#start the thingy, basically calling main or whatever
room1()