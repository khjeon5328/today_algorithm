import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
from collections import deque
ans = sys.maxsize
def dfs(y, x):
    global ans, target_y, target_x

    q = deque([[y, x, 0]])
    visited = [[0] * L for _ in range(L)]

    while len(q):
        loc = q.popleft()
        # print(loc)

        if loc[0] == target_y and loc[1] == target_x:
            print(loc[2])
            return

        for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
            ny = loc[0] + dy
            nx = loc[1] + dx
            if 0 <= ny < L and 0 <= nx < L and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append([ny, nx, loc[2] + 1])


T = int(input())
for _ in range(T):
    L = int(input())
    start_y, start_x = map(int, input().split())
    target_y, target_x = map(int, input().split())
    dfs(start_y, start_x)
