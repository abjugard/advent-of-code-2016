import pprint
from santas_little_helpers import *
from operator import itemgetter
from collections import Counter
import string
import re

regex = re.compile(r'([\w-]+)-([\d]+)\[([a-zA-Z]+)\]')
alphabet = string.ascii_lowercase

class Room:
  def __init__(self, data):
    res = regex.match(data)
    self.name = res.group(1)
    self.sectorid = int(res.group(2))
    self.checksum = res.group(3)

  def count(self):
    c = Counter()
    for char in self.name.replace('-', ''):
      c[char] += 1
    return(c)

  def is_valid(self):
    items = sorted(self.count().items())
    items = sorted(items, reverse=True, key=itemgetter(1))
    word = ''
    for c, count in items:
      word += c
    return(word[:len(self.checksum)] == self.checksum)

  def shifted(self):
    shift = self.sectorid % len(alphabet)
    shifted = alphabet[shift:] + alphabet[:shift]
    table = {ord(x): y for (x, y) in zip(alphabet, shifted)}
    return(self.name.translate(table).replace('-',' '))

if __name__ == '__main__':
  result = 0
  for room in get_data(4, [('replace', (r'\s', '')), ('func', Room)]):
    if room.is_valid():
      # challenge 2
      if room.shifted() == 'northpole object storage':
        print('Found it!', room.sectorid)
      result += room.sectorid
  # challenge 1
  print(result)
