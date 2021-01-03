import sys


sys.stdin = open('input.txt')

N = int(input())
from collections import deque
sequence = deque()
for _ in range(N):
    sequence.append(int(input()))
stack = deque()
ans = deque()
i = 1
while len(sequence):
    n = sequence.popleft()
    if len(stack):
        if stack[-1] == n:
            stack.pop()
            ans.append('-')
            continue
    while i != n:
        stack.append(i)
        ans.append('+')
        i += 1
        if i > N:
            sequence.clear()
            break
    else:
        ans.append('+')
        ans.append('-')
        i += 1
# print(stack)
if len(stack):
    print('NO')
else:
    for i in ans:
        print(i)
