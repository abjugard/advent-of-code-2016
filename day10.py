from santas_little_helpers import *
import pprint
import re

give_re = re.compile(
  r'bot (?P<bot>\d+) gives low to (?P<low_dest>\w+) (?P<low>\d+) and high to (?P<high_dest>\w+) (?P<high>\d+)'
  )
get_re = re.compile(r'value (?P<value>\d+) goes to bot (?P<bot>\d+)')
pp = pprint.PrettyPrinter()

output = {}
bot = {}

class Bot:
  def __init__(self, data):
    self.id = int(data['bot'])
    self.low_dest = data['low_dest'][0] + data['low']
    self.high_dest = data['high_dest'][0] + data['high']
    self.chips = []

  def add(self, val):
    self.chips.append(val)
    if len(self.chips) is 2:
      self.give_chips()

  def give_chips(self):
    high = max(self.chips)
    low = min(self.chips)
    # challenge 1
    if high is 61 and low is 17:
      print('bot', str(self.id), 'compares 61 and 17')
    self.chips = []
    self.give(self.low_dest, low)
    self.give(self.high_dest, high)

  def give(self, to, val):
    def parse(to):
      t = to[0]
      return(t, int(to[1:]))
    dest, no = parse(to)
    if dest is 'o':
      if no in output:
        output[no].append(val)
      else:
        output[no] = [val]
    else:
      bot[no].add(val)

def fmt(line):
  if line.startswith('bot'):
    d = give_re.match(line).groupdict()
    d['type'] = 'instructions'
  else:
    d = get_re.match(line).groupdict()
    d['type'] = 'start'
  return(d)

if __name__ == '__main__':
  ops = [('replace', (r'\n', '')), ('func', fmt)]
  data = get_data(10, ops)
  starting = []
  for d in data:
    if d['type'] is 'instructions':
      bot_id = int(d['bot'])
      bot[bot_id] = Bot(d)
    else:
      del(d['type'])
      starting.append(d)

  for d in starting:
    bot[int(d['bot'])].add(int(d['value']))

  # challenge 2
  print(output[0][0]*output[1][0]*output[2][0])
