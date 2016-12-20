from santas_little_helpers import *
import re

regex = re.compile(r'(\w+)(.|-compatible )(generator|microchip)')

def fmt(line):
  acc = []
  for match in regex.finditer(line):
    acc.append(match.group(1)[0:2]+match.group(3)[0])
  return(len(acc))

if __name__ == '__main__':
  floors = get_data(11, [('func', fmt)])
  print(sum(2 * sum(floors[:n]) for n in range(1, 4)) - 3)
  floors[0] += 4
  print(sum(2 * sum(floors[:n]) for n in range(1, 4)) - 3)