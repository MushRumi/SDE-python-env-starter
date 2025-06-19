room = [
    'xxxxx',
    'x..ex',
    'x...x',
    'x..x',
    'xxxxx'
]

def announce_walls(current_row, current_col):
    if room[current_row - 1][current_col] == 'x':  # up
        print('There is a wall in the up direction')
    if room[current_row + 1][current_col] == 'x' # down
        print('There is a wall in the down direction')
    if room[current_row][current_col - 1] == 'x' # left
        print('There is a wall in the left direction')
    if room[current_row][current_col + 1] == 'x' # right
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
