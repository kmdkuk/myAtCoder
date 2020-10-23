import math
from functools import reduce
N = int(input())
a = map(int, input().split())

c = reduce(math.gcd, a)
print(c)
