import math
import pdb

def new_fraction(sq, whole, num, den_part):
  new_den = sq - den_part**2
  new_den /= num
  new_whole = 0
  num_part = abs(den_part) 
  while math.sqrt(sq) + num_part - new_den > 0:
    num_part -= new_den
    new_whole += 1
  return new_whole, num_part, new_den

def count_all(sq):
  whole_part = int(math.sqrt(sq))
  num = 1
  den_part = -whole_part
  while True:
    whole_part, den_part, num = new_fraction(sq, whole_part, num, den_part)
    yield (whole_part, den_part, num)

def gen(sq):
  for whole, den, num in count_all(sq):
    yield whole

def has_one_period(ls):
  for i in ls[:27]:
    if i != ls[0]:
      return False
  return True

def has_period(ls, length):
  if length == 1:
    return has_one_period(ls)
  a = 0
  b = length
  for l in xrange(4):
    for i in xrange(length):
      if ls[a + i] != ls[b + l*length + i]:
        return False
  return True

def get_period(ls, max):
  if has_one_period(ls):
    return 1
  for length in reversed(xrange(1, max)):
    h = has_period(ls, length)
    if h:
      for n in [2,3,5,7,11,13,17,19,23]:
        if length % n == 0:
          p = get_period(ls, length / n + 1)
          if p: return p
      return length

  return None
 
SEQUENCE_LENGTH = 1971
MAX_PERIOD = 291

N = 10000

def main():
  ans = 0
  for i in xrange(2, N+1):
    if i % 500 == 0: print i
    if math.sqrt(i).is_integer():
      continue
    g = gen(i)
    ls = [g.next() for _ in xrange(SEQUENCE_LENGTH)]
    period = get_period(ls, MAX_PERIOD)
    print i, ls[:20], period
    if period % 2 != 0:
      ans += 1
  print ans

if __name__ == '__main__':
  main()
