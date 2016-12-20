from santas_little_helpers import *
import pprint
import time

regs = {}

def cpy(args):
  val, reg = args
  if val in regs:
    val = regs[val]
  regs[reg] = val
  return 1

def jnz(args):
  condition, distance = args
  if condition not in regs:
    return distance
  if regs.get(condition) != 0:
    return distance
  return 1

def inc(reg):
  regs[reg] += 1
  return 1

def dec(reg):
  regs[reg] -= 1
  return 1

def setup(line):
  instrs = {
    'cpy': cpy,
    'jnz': jnz,
    'inc': inc,
    'dec': dec
  }
  instr = line[0:3]
  args = line[4:].split(' ')
  if args[0].isdigit():
    args[0] = int(args[0])
  if instr == 'jnz':
    args[1] = int(args[1])
  args = tuple(args)
  if len(args) == 1:
    args = args[0]
  return (instrs[instr], args)

def run(stack):
  pc = 0
  while pc < len(stack):
    instr, args = stack[pc]
    pc += instr(args)

if __name__ == '__main__':
  for c in 'abcd':
    regs[c] = 0
  ops = [('replace', (r'\n', '')), ('func', setup)]
  stack = get_data(12, ops)
  start_time = time.time()
  run(stack)
  print(regs['a'])
  print("--- %s seconds ---" % (time.time() - start_time))

  # challenge 2
  for c in 'abcd':
    regs[c] = 0
  regs['c'] = 1
  start_time = time.time()
  run(stack)
  print(regs['a'])
  print("--- %s seconds ---" % (time.time() - start_time))
