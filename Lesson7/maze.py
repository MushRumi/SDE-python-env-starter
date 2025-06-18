room = [
  'xxxxx',
  'x..ex',
  'x...x',
  'xp..x',
  'xxxxx',
]

playerrow = 3
playercol = 1

print('Welcome to the maze!')

#direction should be up, down, left, right
def move(current_row, current_col):
    while True:
        direction = input("Where do you want to move? [Up], [Down], [Left] , [Right] ").lower()

        new_row = current_row
        new_col = current_col
  
        if direction == 'up' or direction == 'u':
            new_row -= 1
        elif direction == 'down' or direction == 'd':
            new_row += 1
        elif direction == 'left' or direction == 'l':
            new_col -= 1
        elif direction == 'right' or direction == 'r':
            new_col += 1
        else:
            print("You did not choose a direction! [Up], [Down], [Left] , [Right]")
            continue
      #thingy that checks for a wall/keeps the game going or ends it

        desiredSpace = room[new_row][new_col]

        if desiredSpace == 'x':
            print("That is a wall.")
            continue
        elif desiredSpace == '.':
            print("You move into that direction.")
            return new_row, new_col, False
        elif desiredSpace =='e':
            print("You reached the exit.")
            return new_row, new_col, True


won = False
while won == False:
    playerrow, playercol, has_won = move(playerrow, playercol)