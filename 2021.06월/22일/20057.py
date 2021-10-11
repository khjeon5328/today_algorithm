import sys


sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
print(arr)
y = x = N//2
print(y, x)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(y, x, d):
    ny = y + dy[d]
    nx = x + dx[d]
    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
        pass


move(y, x, 0)