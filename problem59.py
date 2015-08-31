import itertools

def decrypt(s, key):
  ret = []
  for i, o in enumerate(s):
    ret.append(o ^ key[i % len(key)])
  return ret

def find_keys(s):
  p = itertools.permutations(xrange(ord('a'), ord('z')+1), 3)
  ret = []
  tests = ['have', 'the', 'to']
  tests = [(test, [c for c in test]) for test in tests] 
  keys = []
  for key in p:
    key_found = False
    tests_passed = {}
    for i, ascii_char in enumerate(s):
      ret.append(chr(ascii_char ^ key[i % len(key)]).lower())
      for name, test in tests:
        if ret[-len(test):] == test:
          tests_passed[name] = 1
    if len(tests_passed) == len(tests):
      keys.append(key)
  return keys

def main():
  f = open('p059_cipher.txt')
  s = [int(c) for c in f.read().strip().split(',')]
  
  keys = find_keys(s)
  for key in keys:
    decrypted = decrypt(s, key)
    print ''.join([chr(c) for c in key])
    print ''.join(chr(c) for c in decrypted)
    print sum(decrypted)

if __name__ == '__main__':
  main()
