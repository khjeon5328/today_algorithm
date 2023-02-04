import sys


sys.stdin = open('input.txt')

N, K = map(int, input().split())
import collections
q = collections.deque()
for i in range(1, N+1):
    q.append(i)
ans = []
cnt = 1
while len(q):
    if cnt == K:
        ans.append(q.popleft())
        cnt = 1
    else:
        q.append(q.popleft())
        cnt += 1
print('<',end="")
for i in ans:
    if i != ans[-1]:
        print(i, end=", ")
    else:
        print(i, end="")
print('>', end="")