import re, json
from pathlib import Path
from requests import request
from datetime import date

with open('config.json', 'r') as f:
  config = json.load(f)
today = date.today().day
datadir = Path('data')

def getdata(day=today, strip=None, replace='', spc=None, func=None):
  ops = []
  if strip:
    ops.append(('replace', (strip, replace)))
  if spc:
    ops.append(('split', spc))
  if func:
    ops.append(('func', func))
  return(get_data(day, ops))

def get_data(day=today, ops=[]):
  if not datadir.exists():
    datadir.mkdir()
  def format_line(line, ops):
    for op, args in ops:
      if op == 'replace':
        line = re.sub(args[0], args[1], line)
      if op == 'split':
        line = line.split(args)
      if op == 'func':
        line = args(line)
    return(line)

  def save_daily_input(day=today):
    url = 'http://adventofcode.com/2016/day/{}/input'.format(day)
    res = request('GET', url, cookies=config)
    with path.open('wb') as fd:
      for chunk in res.iter_content(chunk_size=128):
        fd.write(chunk)

  path = datadir / 'day{}'.format(day)
  if not path.exists():
    save_daily_input(day)
  data = []
  with path.open() as f:
    for line in f.readlines():
      line = format_line(line, ops)
      data.append(line)
  return(data)
