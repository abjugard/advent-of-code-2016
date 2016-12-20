from santas_little_helpers import *
import hashlib

possible = {'b','c','d','e','f'}

if __name__ == '__main__':
  ops = [('replace', (r'\n', ''))]
  data = get_data(17, ops)[0]
  # data = 'ulqzkmiv'
  maximum = 0
  solution = ''
  stack = [(data, (0,0))]
  print(stack)

  while stack:
    code, p = stack.pop(0)
    x, y = p
    # print(code, p)
    h = hashlib.md5(code.encode('utf-8')).hexdigest()

    if(x == 3 and y == 3):
      if(len(code) > maximum):
        maximum = len(code)
        solution = code
      continue
    else:   
      if y > 0 and h[0] in possible:
        stack.append((code + 'U', (x, y - 1)))
      if y < 3 and h[1] in possible:
        stack.append((code + 'D', (x, y + 1)))
      if x > 0 and h[2] in possible:
        stack.append((code + 'L', (x - 1, y)))
      if x < 3 and h[3] in possible:
        stack.append((code + 'R', (x + 1, y)))
  print(maximum-len(data), solution)
