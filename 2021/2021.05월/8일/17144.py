import sys
from pprint import pprint

sys.stdin = open('input.txt')

input = sys.stdin.readline

R, C, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

# pprint(arr)

machine = []
for i in range(R):
    if arr[i][0] == -1:
        machine.append(i)

def bfs():
    visited = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if x == 0 and y in machine:
                continue
            if arr[y][x]:
                cnt = 0
                for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < C and 0 <= ny < R and not arr[ny][nx] == -1:
                        cnt += 1
                        visited[ny][nx] += (arr[y][x] // 5)
                arr[y][x] -= cnt*(arr[y][x] // 5)
    for y in range(R):
        for x in range(C):
            if visited[y][x]:
                arr[y][x] += visited[y][x]
    # pprint(arr)
def wind():
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    i = 0
    y = machine[0] -1
    x = 0
    while True:
        nx = dx[i%4] + x
        ny = dy[i%4] + y
        if 0 <= nx < C and 0 <= ny <= machine[0]:
            if arr[ny][nx] == -1:
                arr[y][x] = 0
                break
            arr[y][x] = arr[ny][nx]
            x = nx
            y = ny
        else:
            i += 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    i = 0
    y = machine[1] + 1
    x = 0
    while True:
        nx = dx[i%4] + x
        ny = dy[i%4] + y
        if 0 <= nx < C and machine[1] <= ny < R:
            if arr[ny][nx] == -1:
                arr[y][x] = 0
                break
            arr[y][x] = arr[ny][nx]
            x = nx
            y = ny
        else:
            i += 1



for _ in range(T):
    bfs()
    # pprint(arr)
    wind()
    # pprint(arr)
    # print('===========================')
ans = 0
for y in range(R):
    for x in range(C):
        if arr[y][x] and arr[y][x] != -1:
            ans += arr[y][x]
print(ans)