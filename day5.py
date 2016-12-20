import hashlib
import time
from itertools import count
from santas_little_helpers import *

def find_hash(data):
  # m = hashlib.md5(data)
  for i in count():
    h = hashlib.md5(data+str(i).encode())
    thehash = h.hexdigest()
    if thehash.startswith('00000'):
      yield(thehash)

if __name__ == '__main__':
  start_time = time.time()
  ops = [('replace', (r'\s', ''))]
  data = get_data(5, ops)[0]
  password = [None]*8
  for i, thehash in enumerate(find_hash(data.encode())):
    pos = int(thehash[5], 16)
    value = thehash[6]
    # challenge 1
    # pos = i
    # value = thehash[5]
    if pos in range(8):
      # challenge 2
      if not password[pos]:
        password[pos] = value
        if not None in password:
          break
  print(''.join(password))
  print("--- {}s seconds ---".format(time.time() - start_time))
