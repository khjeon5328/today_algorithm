import sys
from pprint import pprint

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

arr = [list(input().split()) for _ in range(N)]

# print(arr)

teacher = []
for y in range(N):
    for x in range(N):
        if arr[y][x] == 'T':
            teacher.append((y, x))
ans = 'NO'

def bfs(arr):
    global ans
    for y, x in teacher:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            while 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] == 'O':
                    break
                elif arr[ny][nx] == 'S':
                    # pprint(arr)
                    return 
                nx += dx
                ny += dy
    # pprint(arr)
    ans = 'YES'

def dfs(n, l, arr):
    global ans

    if ans == 'YES':
        return
    if n == 3:
        bfs(arr)
        return

    i = l // N
    j = l % N

    for y in range(i, N):
        for x in range(j, N):
            if arr[y][x] == 'X':
                arr[y][x] = 'O'
                dfs(n+1, l+1, arr)
                arr[y][x] = 'X'
dfs(0, 0, arr)
print(ans)