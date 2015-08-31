import math
import itertools
import copy
 
primes = [2, 3]

def is_prime(n):
  sqrt_n = math.sqrt(n)
  for i in primes:
    if n % i == 0:
      return False
    if i >= sqrt_n:
      break
  if primes[-1] < sqrt_n:
    for i in xrange(primes[-1]+1, int(sqrt_n)+1):
      if n % i == 0:
        return False
  return True
 
def make_primes(n):
  for i in xrange(5, n):
    if is_prime(i):
      primes.append(i)

make_primes(20000)

def join(a, b):
  return a * 10**int(math.log10(b) + 1) + b

def main():
  not_primes = set()
  for i1, p1 in enumerate(primes):
    for i2, p2 in enumerate(primes[i1+1:]): 
      if not is_prime(join(p1, p2)) or not is_prime(join(p2, p1)):
        continue
      for i3, p3 in enumerate(primes[i1+i2+1:]):
        if not is_prime(join(p2, p3)) or not is_prime(join(p3, p2)):
          continue
        if not is_prime(join(p1, p3)) or not is_prime(join(p3, p1)):
          continue
        for i4, p4 in enumerate(primes[i1+i2+i3+1:]):
          if not is_prime(join(p1, p4)) or not is_prime(join(p4, p1)):
            continue
          if not is_prime(join(p2, p4)) or not is_prime(join(p4, p2)):
            continue
          if not is_prime(join(p3, p4)) or not is_prime(join(p4, p3)):
            continue
          for p5 in primes[i1+i2+i3+i4+1:]:
            if not is_prime(join(p1, p5)) or not is_prime(join(p5, p1)):
              continue
            if not is_prime(join(p2, p5)) or not is_prime(join(p5, p2)):
              continue
            if not is_prime(join(p3, p5)) or not is_prime(join(p5, p3)):
              continue
            if not is_prime(join(p4, p5)) or not is_prime(join(p5, p4)):
              continue
            print p1, p2, p3, p4, p5
            print sum([p1, p2, p3, p4, p5])

if __name__ == '__main__':
  main()
