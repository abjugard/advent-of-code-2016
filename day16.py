from santas_little_helpers import *

def reverse(data):
  return data[::-1]

def invert(data):
  new_data = ''
  for c in data:
    new_data += '0' if c == '1' else '1'
  return new_data

def expand(data):
  return data + '0' + invert(reverse(data))

def solve(dummy, disk_size):
  while len(dummy) < disk_size:
    dummy = expand(dummy)
  dummy = dummy[:disk_size]
  checksum = ''
  while True:
    data = dummy if checksum is '' else checksum
    checksum = ''
    for i in range(0, len(data), 2):
      checksum += '1' if data[i] == data[i+1] else '0'
    if len(checksum) % 2 is not 0:
      break
  return checksum

if __name__ == '__main__':
  ops = [('replace', (r'\n', ''))]
  dummy = get_data(16, ops)[0]
  print('Part 1:', solve(dummy, 272))
  print('Part 2:', solve(dummy, 35651584))
