import sys
from pprint import pprint

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
# print(arr)
for _ in range(M):
    a, b = map(int, input().split())
    if b not in arr[a]:
        arr[a].append(b)
    if a not in arr[b]:
        arr[b].append(a)

# pprint(arr) 
from collections import deque
minV = 987654321
ans = 0
def bfs(k, v):
    global ans, minV
    visited = [0] *(N+1)
    q = deque()
    q.append([k, v])
    visited[k] = 1
    while q:
        v = q.popleft()    

        for i in arr[v[0]]:
            if not visited[i]:
                visited[i] = v[1]
                q.append([i, v[1]+1])

    if sum(visited) < minV:
        minV = sum(visited)
        ans = k

for i in range(1, N+1):
    bfs(i, 1)
print(ans)