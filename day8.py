from santas_little_helpers import *
from collections import deque
import re

rectre = re.compile(r'(\d+)x(\d+)')
rotre = re.compile(r'\w+=(\d+)by(\d+)')

disp_char = '█'

def fmt(line):
  if line.startswith('rect'):
    op = rect
    r = rectre.match(line[len('rect'):])
  else:
    op = rotaterow if 'row' in line else rotatecol
    r = rotre.match(line)
  args = (int(r.group(1)), int(r.group(2)))
  return((op, args))

def rect(m, point):
  x, y = point
  for row in range(y):
    for col in range(x):
      m[row][col] = disp_char
  return(m)

def rotaterow(disp, args):
  row, by = args
  deq = deque(disp[row])
  deq.rotate(by)
  disp[row] = list(deq)
  return(disp)

def transpose(m):
  return([list(i) for i in zip(*m)])

def rotatecol(disp, args):
  m = transpose(disp)
  m = rotaterow(m, args)
  return(transpose(m))

def print_disp(m):
  print('  '+''.join([s*10 for s in ' 1234']))
  print('  '+'0123456789'*5)
  for i, row in enumerate(m):
    print(str(i) + ' ' + ''.join(row))

if __name__ == '__main__':
  ops = [('replace', (r'\s', '')), ('func', fmt)]
  data = get_data(8, ops)
  disp = []
  for y in range(6):
    row = []
    for x in range(50):
      row.append(' ')
    disp.append(row)
  for op, args in data:
    disp = op(disp, args)

  print_disp(disp)
  count = 0
  for row in range(len(disp)):
    for col in range(len(disp[row])):
      if disp[row][col] == disp_char:
        count += 1

  print(count)
