import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)
# print(arr)
ans = [0] * (N+1)
from collections import deque

def bfs(idx):
    global maxV, ans
    q = deque([idx])
    visited = [0] * (N+1)
    visited[idx] = 1
    cnt = 1
    while q:
        hack = q.popleft()
        for i in arr[hack]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                q.append(i)
    ans[idx] = cnt
    

for i in range(1, N+1):
    bfs(i)
maxV = max(ans)
for i in range(1, N+1):
    if ans[i] == maxV:
        print(i, end=" ")