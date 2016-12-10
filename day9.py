from santas_little_helpers import *
import re

regex = re.compile(r'\((\d+)x(\d+)\)')

def parse_string(data):
  if len(data) == 0:
    return(0)
  ret = 0
  end = 0
  instruction = regex.match(data)
  if instruction:
    start = instruction.span()[1]
    end = start + int(instruction.group(1))
    reps = int(instruction.group(2))
    sub_length = parse_string(data[start:end])
    ret += sub_length * reps
  else:
    ret += len(data.partition("(")[0])
    end += ret
  return(ret + parse_string(data[end:]))

if __name__ == '__main__':
  ops = [('replace', (r'\n', ''))]
  data = get_data(9, ops)[0]
  print(parse_string(data))
