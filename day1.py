import pprint
from santas_little_helpers import *

moves = [0]*4

path = set()

def current_pos():
  return (moves[0]-moves[2], moves[1]-moves[3])

def distance(pos):
  n, w = pos
  return abs(n) + abs(w)

if __name__ == '__main__':
  pp = pprint.PrettyPrinter()
  data = getdata(1, strip=r'\s', spc=',')[0]
  c_dir = 0
  for movement in data:
    turn = -1 if movement[0] == 'L' else 1
    steps = int(movement[1:])
    c_dir = (c_dir + turn) % 4
    for _ in range(steps):
      moves[c_dir] += 1
      if current_pos() in path:
        print('been here!', str(current_pos()), 'distance:', str(distance(current_pos())))
      else:
        path.add(current_pos())

  pp.pprint(distance(current_pos()))
