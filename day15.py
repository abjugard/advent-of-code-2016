from santas_little_helpers import *
import re
import pprint

regex = re.compile(r'has (\d+)[a-z\s;(=0),]+(\d+)')

def fmt(line):
  m = regex.search(line)
  line = ((int(m.group(2)), int(m.group(1))))
  return line

def rotate(discs):
  new_discs = []
  for pos, mod in discs:
    new_pos = (pos + 1) % mod
    new_discs.append((new_pos, mod))
  return new_discs

def fall_fails(discs):
  for i, disc in enumerate(discs):
    if not in_correct_position(disc, i+1):
      return True
  return False

def in_correct_position(disc, steps):
  return ((disc[0] + steps) % disc[1]) == 0

if __name__ == '__main__':
  global t
  t = 0
  ops = [('func', fmt)]
  discs = get_data(15, ops)
  while fall_fails(discs):
    discs = rotate(discs)
    t += 1
  print('Part 1:', t)
  t = 0
  discs = get_data(15, ops)
  discs.append((0, 11))
  while fall_fails(discs):
    discs = rotate(discs)
    t += 1
  print('Part 2:', t)
