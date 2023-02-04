import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

if d == 3:
    d = 1
elif d == 1:
    d = 3

from collections import deque

ans = 0
def bfs(r, c, d):
    global ans, arr

    q = deque([(r, c, d)])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    arr[r][c] = -1
    ans += 1
    # print(q)
    while q:
        loc = q.popleft()
        # print(loc)
        loc_y = loc[0]
        loc_x = loc[1]
        d = loc[2]

        for i in range(d, d+4):
            ny = loc_y + dy[i%4]
            nx = loc_x + dx[i%4]
            if 0<= nx < M and 0 <= ny < N and not arr[ny][nx]:
                arr[ny][nx] = -1
                ans += 1
                q.append((ny, nx, (i+1)%4))
                break
            if i == d+3:
                q.append((loc_y + dy[(d+1)%4], loc_x + dx[(d+1)%4], d))
                if arr[loc_y + dy[(d+1)%4]][loc_x + dx[(d+1)%4]]  == 1:
                    print(ans)
                    return

bfs(r, c, d)
# print(r, c, d)
# from pprint import pprint
# pprint(arr)
# print(ans)