room = [
  'xxxxx',
  'x..ex',
  'x...x',
  'x...x',
  'xxxxx',
]

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

  return [new_row, new_col]

new_position = move(2, 2, 'up')
# At this point, new_position should be the list [1, 2]

print(new_position)