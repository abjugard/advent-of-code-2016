from santas_little_helpers import *

visited = set()
favourite_number = get_data(13, [('replace', (r'\n', '')), ('func', int)])[0]

def permutations(x, y):
  return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def is_wall(x, y):
  value = x*x + 3*x + 2*x*y + y + y*y + favourite_number
  return bin(value).count('1') % 2 == 1

if __name__ == '__main__':
  visited.add((1, 1))
  steps = 0
  unchecked = visited
  while (31, 39) not in visited:
    places_to_check = unchecked.copy()
    unchecked = set()
    for o_x, o_y in places_to_check:
      for x, y in permutations(o_x, o_y):
        if x < 0 or y < 0 or (x, y) in visited or is_wall(x, y):
          continue
        visited.add((x, y))
        unchecked.add((x, y))
    steps += 1
    if (31, 39) in unchecked:
      print('Part 1:', steps)
    if steps == 50:
      print('Part 2:', len(visited))