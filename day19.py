from santas_little_helpers import *

n = 0

class Elf():
  def __init__(self, right=None):
    global n
    self.left = None
    self.right = right
    n += 1
    self.n = n

  def leave_circle(self):
    self.left.right = self.right
    self.right.left = self.left
    return self.left

if __name__ == '__main__':
  ops = [('replace', (r'\n', '')), ('func', int)]
  elves = get_data(19, ops)[0]
  first = Elf()
  last = first
  for i in range(elves-1):
    new_elf = Elf(right=last)
    last.left = new_elf
    last = new_elf
  last.left = first
  first.right = last
  # part 1
  # current = first.left 
  # part 2
  current = first
  for _ in range(elves // 2):
    current = current.left

  while elves > 1:
    current = current.leave_circle()
    # part 1
    # current = current.left
    # part 2
    if elves % 2 == 1:
      current = current.left
    elves -= 1
  print(current.n)
