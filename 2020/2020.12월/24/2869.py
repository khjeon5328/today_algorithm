import sys


sys.stdin = open('input.txt')

import math
a, b, v = map(int, input().split())
cnt = 1

if a >= v:
    print(cnt)
else:
    v -= a
    diff = a-b
    print(1 + math.ceil(v/diff))

