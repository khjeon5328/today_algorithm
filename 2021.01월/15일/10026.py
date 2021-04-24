import sys

sys.stdin = open('input.txt')

# input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(map(str, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
# print(arr)
def dfs(y, x, color, visited, arr):
    q = deque([[y, x]])

    while len(q):
        loc = q.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny = loc[0] + dy
            nx = loc[1] + dx
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and arr[ny][nx] == color:
                q.append([ny, nx])
                visited[ny][nx] = 1

def dfs2(y, x, color, visited, arr):
    q = deque([[y, x]])
    color2 = ''
    if color == 'R':
        color2 = 'G'
    elif color == 'G':
        color2 = 'R'

    while len(q):
        loc = q.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny = loc[0] + dy
            nx = loc[1] + dx
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and (arr[ny][nx] == color or arr[ny][nx] == color2):
                q.append([ny, nx])
                visited[ny][nx] = 1



normal = 0
blind = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            dfs(y, x, arr[y][x], visited, arr)
            normal += 1
        if not visited2[y][x]:
            dfs2(y, x, arr[y][x],visited2, arr)
            blind += 1
        
print(normal, blind)