from __future__ import division
from prime_gen import PrimeGen

def spiral_corners(side_length, start):
  if side_length == 1: return [1], start
  corners = []
  number = start

  number += side_length - 2
  corners.append(number)

  number += side_length - 1
  corners.append(number)

  number += side_length - 1
  corners.append(number)

  number += side_length - 1

  corners.append(number)
  return corners, number

def main():
  side = 3
  number = 2
  primes = 0
  nonprimes = 1 # [1]
  prime_gen = PrimeGen()
  
  while True:
    corners, finish = spiral_corners(side, number)
    for corner in corners:
      if prime_gen.is_prime(corner):
        primes += 1
      else:
        nonprimes += 1
    number = finish + 1
    ratio = primes / (primes + nonprimes)
    if ratio < 0.1:
      print side
      break
    side += 2

if __name__ == '__main__':
  main()
