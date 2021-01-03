import sys


sys.stdin = open('input.txt')
from collections import deque

N = int(input())
stack = deque()
hap = 0
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))
