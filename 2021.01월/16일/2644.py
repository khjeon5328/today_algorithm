import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

from collections import deque

n = int(input())
_from, _to = map(int, input().split())
m = int(input())

arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)
# print(arr)
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

ans = -1
def dfs(k, depth):
    global ans

    visited[k] = 1
    if k == _to:
        ans = depth
        return 

    for i in arr[k]:
        if not visited[i]:
            dfs(i, depth + 1)
dfs(_from, 0)
print(ans)

