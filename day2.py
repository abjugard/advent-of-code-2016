import pprint
from santas_little_helpers import *

# Part 1
# npad = {
#   2: ['1', '2', '3'],
#   1: ['4', '5', '6'],
#   0: ['7', '8', '9']
# }

# Part 2
npad = {
  4: [None, None, '1', None, None],
  3: [None, '2',  '3',  '4', None],
  2: ['5',  '6',  '7',  '8',  '9'],
  1: [None, 'A',  'B',  'C', None],
  0: [None, None, 'D', None, None]
}

def get_next_pos(c, m):
  h, w = get_pos(c)
  if m == 'R':
    w = min(len(npad[h]), w+1)
  if m == 'L':
    w = max(0, w-1)
  if m == 'U':
    h = min(len(npad[h]), h+1)
  if m == 'D':
    h = max(0, h-1)
  return (h, w)

def get_pos(c):
  for h in npad:
    for w, v in enumerate(npad[h]):
      if c == v:
        return (h, w)
  return None

def get_c(line, c):
  # print(get_pos(c))
  for m in line:
    # print(c, m)
    t_h, t_w = get_next_pos(c, m)
    try:
      if npad[t_h][t_w]:
        c = npad[t_h][t_w]
    except Exception as e:
      pass
    # print(c)
  return c

if __name__ == '__main__':
  pp = pprint.PrettyPrinter()
  data = getdata(2, strip=r'\s')
  # print(data)
  c = '5'
  ret = ''
  for line in data:
    c = get_c(line, c)
    ret += c
  print(ret)
