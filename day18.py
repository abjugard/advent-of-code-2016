from santas_little_helpers import *

def calculate_tile(surrounding):
  return '^' if surrounding in ['^^.', '.^^', '^..', '..^'] else '.'

def get_tile(row, col):
  if col < 0 or col >= len(row):
    return '.'
  else:
    return row[col]

def solve(tiles, depth):
  tiles = list(tiles)
  for row in range(depth-1):
    next_row = []
    for col in range(len(tiles[row])):
      surrounding = ''.join([get_tile(tiles[row], col+i) for i in [-1, 0, 1]])
      next_row.append(calculate_tile(surrounding))
    tiles.append(''.join(next_row))
  return sum([sum(1 for t in row if t is '.') for row in tiles])

if __name__ == '__main__':
  ops = [('replace', (r'\n', ''))]
  tiles = get_data(18, ops)
  print('Part 1:', solve(tiles, 40))
  print('Part 2:', solve(tiles, 400000))
  # print(tiles)
