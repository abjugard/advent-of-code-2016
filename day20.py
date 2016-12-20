from santas_little_helpers import *
import time

START, STOP = 1, -1

def join_ranges(data):
  balance = 0
  for value, direction in data:
    if balance is 0:
      x = value
    balance += direction
    if balance is 0:
      yield x + 1, value - 1

def fmt(line):
  values = line.split('-')
  start = int(values[0])
  stop = int(values[1])
  return [(start - 1, START), (stop + 1, STOP)]

if __name__ == '__main__':
  ops = [('replace', (r'\n', '')), ('func', fmt)]
  raw_data = get_data(20, ops)
  data = []
  for row in raw_data:
    data.append(row[0])
    data.append(row[1])
  data = sorted(data)
  start_time = time.time()
  solution = list(join_ranges(data))
  print('Part 1:', solution[0][1]+1)
  blacklisted = sum([(b-a)+1 for a, b in solution])
  print('Part 2:', 4294967295 + 1 - blacklisted)
  print("--- {}s seconds ---".format(time.time() - start_time))
