import re
import pprint
from santas_little_helpers import *

regex = re.compile(r'(\w+)*(\[[\w]+\])*')

def contains_abba(string):
  for i in range(len(string)-3):
    a = string[i]
    b = string[i+1]
    if b == a:
      continue
    abba = a+b+b+a
    if string[i:i+4] == abba:
      return(True)
  return(False)

def flip_bab(s):
  return(s[1]+s[0]+s[1])

def find_babs(string):
  babs = []
  for aba in find_abas(string[1:-1]):
    babs.append(flip_bab(aba))
  return(babs)

def find_abas(string):
  abas = []
  for i in range(len(string)-2):
    a = string[i]
    b = string[i+1]
    if b == a:
      continue
    aba = a+b+a
    if string[i:i+3] == aba:
      abas.append(aba)
  return(abas)

if __name__ == '__main__':
  ops = [('replace', (r'\s', ''))]
  data = get_data(7, ops)
  count = 0
  for ip in data:
    matchlist = []
    for matches in regex.findall(ip):
      for group in matches:
        if len(group) < 1:
          continue
        matchlist.append(group)

    abas = []
    babs = []
    for group in matchlist:
      if group.startswith('['):
        babs.extend(find_babs(group))
      if not group.startswith('['):
        abas.extend(find_abas(group))
    abas = set(abas)
    babs = set(babs)
    if len(abas.intersection(babs)) > 0:
      count += 1
  print(count)
