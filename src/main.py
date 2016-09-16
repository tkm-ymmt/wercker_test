import sys
sys.path = sys.path + ['.']

from lib.Divisors import Divisors

d = Divisors(3, 20, 6)
print(d.length)
