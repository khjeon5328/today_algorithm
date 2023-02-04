import sys
from pprint import pprint


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
arr = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    arr[y-1][x-1] = 'a'
L = int(input())
move = [0] * 10001
for _ in range(L):
    X, C = input().split()
    move[int(X)] = C


from collections import deque

def bfs():
    time = 0
    visited = deque([(0, 0)])
    q = deque([(0, 0)])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    direction = 0

    while q:
        y, x = q.popleft()
        if move[time]:
            if move[time] == 'L':
                direction += 3
                direction %= 4
            else:
                direction += 1
                direction %= 4
        ny, nx = y + dy[direction], x + dx[direction]

        if 0 <= ny < N and 0 <= nx < N and not arr[ny][nx] == 's':
            if not arr[ny][nx] == 'a':
                i, j = visited.popleft()
                arr[i][j] = 0
            arr[ny][nx] = 's'
            q.append((ny, nx))
            visited.append((ny, nx))
            time += 1
        else:
            print(time + 1)
            return 
bfs()

