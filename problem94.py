from math import *
from fractions import gcd

def main():
  result = 0
  MAX = 100000
  done = False
  for u in xrange(1, MAX):
    for v in xrange(1, u):
      if gcd(u, v) == 1:
        a = 2 * (u**2 - v**2)
        b = u**2 + v**2
        d = abs(b - a)
        if a % d == 0 and b % d == 0:
          P = a/d + 2*b/d
          if P > 10**9:
            done = True
            break
          else:
            result += P
    if done:
      break
  print result
      
if __name__ == '__main__':
  main()
