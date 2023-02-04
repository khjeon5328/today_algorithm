import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
# print(visited)

def dfs(start, n):
    for i in range(N):
        if arr[n][i] and not visited[start][i]:
            visited[start][i] = 1
            dfs(start, i)

for i in range(N):
    dfs(i, i)
# print(visited)
for i in visited:
    print(*i)