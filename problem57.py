expansion_cache = {}

def expansion(n):
  if n == 1: return 3, 2
  if n in expansion_cache:
    return expansion_cache[n]
  else:
    num, den = expansion(n-1)
    num += den
    den, num = num, den
    ret = num + den, den
    expansion_cache[n] = ret
    return ret

def main():
  count = 0
  for i in xrange(1, 1001):
    num, den = expansion(i)
    if len(str(num)) > len(str(den)):
      count += 1
  
  print count

if __name__ == '__main__':
  main()
