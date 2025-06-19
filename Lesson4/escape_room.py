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
        else:
            print('Something beastly has grabbed you by the legs.')
            print('You are dragged down into the depths. Too slow.')
    else:
        timer -= 1
        print('The ground shakes. You get the feeling you are not meant to be here.')
        print('You must hurry.')
        print('')
        if timer > 0:
            room2(timer)
        else:
            print('You overstayed your welcome and fall into the depths.')

#start the thingy, basically calling main or whatever
room1()

room = [
    'xxxxx',
    'x..ex',
    'x...x',
    'x...x',
    'xxxxx'
]

def announce_walls(current_row, current_col):
    if room[current_row - 1][current_col] == 'x':  # up
        print('There is a wall in the up direction')
    if room[current_row + 1][current_col] == 'x': # down
        print('There is a wall in the down direction')
    if room[current_row][current_col - 1] == 'x': # left
        print('There is a wall in the left direction')
    if room[current_row][current_col + 1] == 'x': # right
        print('There is a wall in the right direction')

def move(current_row, current_col, direction):
    new_row = current_row
    new_col = current_col

    if direction == 'up':
        new_row -= 1
    elif direction == 'down':
        new_row += 1
    elif direction == 'left':
        new_col -= 1
    elif direction == 'right':
        new_col += 1
    else:
        print(f'You can not move {direction_choice}. Try up, down, left, or right.')

    if room[new_row][new_col] == 'x':  # Hit a wall!
        print('You can not move that way, there is a wall.')
        return current_row, current_col

    return new_row, new_col

player_row = 2
player_col = 2


while room[player_row][player_col] != 'e':
    direction_choice = input("What direction would you like to move? Your options are: up, down, left, right: ")
    player_row, player_col = move(player_row, player_col, direction_choice)
    print(f'New row is {player_row}')
    print(f'New col is {player_col}')
    announce_walls(player_row, player_col)

print('You escaped! ')
