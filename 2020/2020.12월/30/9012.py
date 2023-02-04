import sys



sys.stdin = open('input.txt')
from collections import deque
N = int(input())

for _ in range(N):
    stack = deque()
    l = list(input())
    for i in l:
        if i == '(':
            stack.append('(')
        else:
            if len(stack):
                stack.pop()
            else:
                stack.append(-1)
                break
    if len(stack):
        print('NO')
    else:
        print('YES')