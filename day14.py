import hashlib
import time
from itertools import count
from santas_little_helpers import *
import re

triple = re.compile(r'(.)\1{2}')

def find_hash(data, hash_more):
  h = hashlib.new('md5')
  # m = hashlib.md5(data)
  for i in count():
    h = hashlib.md5(data+str(i).encode())
    thehash = h.hexdigest()
    if hash_more:
      for _ in range(2016):
        thehash = hashlib.md5(thehash.encode()).hexdigest()
    match = triple.search(thehash)
    if match:
      # print(match.group(1), thehash)
      yield (i, match.group(1), thehash)

def solve(data, hash_more=False):
  for_consideration = []
  secrets = []
  for new_i, char, new_hash in find_hash(data.encode(), hash_more):
    new_considerations = []
    for old_i, check_for, thehash in for_consideration:
      if new_i-old_i < 1001:
        if check_for*5 in new_hash:
          secrets.append((old_i, thehash))
          if len(secrets) >= 64 and secrets[63][0] < new_i-1001:
            return(sorted(secrets)[63])
        else:
          new_considerations.append((old_i, check_for, thehash))
    for_consideration = new_considerations
    for_consideration.append((new_i, char, new_hash))

if __name__ == '__main__':
  ops = [('replace', (r'\n', ''))]
  data = get_data(14, ops)[0]
  start_time = time.time()
  print(solve(data))
  print("--- {}s seconds ---".format(time.time() - start_time))
  start_time = time.time()
  print(solve(data, hash_more=True))
  print("--- {}s seconds ---".format(time.time() - start_time))
