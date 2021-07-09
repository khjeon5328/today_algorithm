import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(input())

tmp = list(map(int, input().split()))
q = deque()
for i in range(N):
    q.append((i, tmp[i]))

ans = [0] * N
cnt = 1
while q:
    n, p = q.popleft()
    if p > 1:
        q.append((n, p-1))
    else:
        ans[n] = cnt
    cnt += 1
print(*ans)