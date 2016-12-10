import time
from collections import Counter
from santas_little_helpers import *

if __name__ == '__main__':
  start_time = time.time()
  ops = [('replace', (r'\s', ''))]
  data = get_data(6, ops)
  counters = []
  for i in range(len(data[0])):
    counters.append(Counter())
  for word in data:
    for i, c in enumerate(word):
      counters[i][c] += 1
  result = ''
  for counter in counters:
    # result += counter.most_common()[0][0] # challenge 1
    lowest = max(counter.values())
    least_common = ''
    for c in counter:
      freq = counter[c]
      if freq < lowest:
        lowest = freq
        least_common = c
    result += least_common
  print(result)
  print("--- {}s seconds ---".format(time.time() - start_time))
