import pprint
from santas_little_helpers import *

def fmt(line):
    del(line[4])
    del(line[0])
    new_line = []
    for el in line:
      new_line.append(int(el))
    return new_line

def fmt2(triangles):
  triangles = [list(i) for i in zip(*triangles)]
  temp = []
  for row in triangles:
    temp.extend(row)
  ret = []
  for count, el in enumerate(temp):
    i = count // 3
    if len(ret) < i+1:
      ret.append([el])
    else:
      ret[i].append(el)
    # print(i, el)
    # if len(ret[i]) == 3:
    #   pp.pprint(ret[i])
  return ret

def is_possible(s):
  test = s[0]+s[1] > s[2]
  test = test and s[1]+s[2] > s[0]
  test = test and s[2]+s[0] > s[1]
  return test

if __name__ == '__main__':
  pp = pprint.PrettyPrinter()
  data = getdata(3, strip=r'\s+', replace=' ', spc=' ', func=fmt)
  data = fmt2(data) # challenge 2
  data = sorted(data)
  pp.pprint(data)
  possible_triangles = 0
  for triangle in data:
    if is_possible(triangle):
      possible_triangles += 1
  pp.pprint(possible_triangles)
