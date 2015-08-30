import math

class PrimeGen(object):
  def __init__(self):
    self._primes = [2, 3]
    self._primes_set = set(self._primes)

  def add_primes(self, until):
    n = self._primes[-1] + 1
    while self._primes[-1] < until:
      if self.is_prime(n, add=False):
        self._primes.append(n)
        self._primes_set.add(n)
      n += 1
    
  def is_prime(self, n, add=True):
    if n == 1:
      return False
    if self._primes[-2] < n < self._primes[-1]:
      return False
    if n in self._primes_set: 
      return True
    if add and self._primes[-1] < n:
      self.add_primes(n)
    for p in self._primes:
      if p > math.sqrt(n):
        break
      if n % p == 0:
        return False
    return True
