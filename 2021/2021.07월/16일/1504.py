import sys
from pprint import pprint

sys.stdin = open('input.txt')

N, E = map(int, input().split())


arr = [[0]*(N+1) for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    arr[b][a] = c

v1, v2 = map(int, input().split())
# print(v1, v2)
# pprint(arr)
visited = [0] * (N+1)

def dfs(n, dist):
    for i in range(1, N+1):
        if arr[i]:
            if not visited[i]:
                dfs(i, arr[i])
            elif visited[i] >= dist + arr[i]:
                visited[i] = dist + arr[i]
                dfs(i, dist + arr[i])





dfs(1, 0)

