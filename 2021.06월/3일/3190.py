import sys
from copy import deepcopy


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
# print(move)

from pprint import pprint
# pprint(arr)

from collections import deque

def bfs(board, ny, nx, isApple, length):
    q = deque([(ny, nx, 1)])
    if isApple:
        while q:
            y, x, n = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == n:
                    board[ny][nx] = n + 1
                    q.append((ny, nx, n + 1))
    else:
        while q:
            y, x, n = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == n:
                    if board[ny][nx] == length:
                        board[ny][nx] = 0
                    else:
                        board[ny][nx] = n + 1
                        q.append((ny, nx, n + 1))
    return board

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(board, second, head, direction, length):
    if move[second]:
        if move[second] == 'L':
            direction += 3
            direction %= 4
        else:
            direction += 1
            direction %= 4
    y = head[0]
    x = head[1]
    ny = y + dy[direction]
    nx = x + dx[direction]

    if 0 <= ny < N and 0 <= nx < N:
        if board[ny][nx] == 'a':
            board[ny][nx] = 1
            length += 1
            new_board = bfs(deepcopy(board), ny, nx, 1, length)
            dfs(new_board, second + 1, (ny, nx), direction, length)
        elif board[ny][nx] == 0:
            board[ny][nx] = 1
            new_board = bfs(deepcopy(board), ny, nx, 0, length)
            dfs(new_board, second + 1, (ny, nx), direction, length)
        # 자기 몸과 부딪쳐서 게임종료
        elif board[ny][nx]:
            print(second + 1)
            return
    else:
        # 벽에 부딪쳐서 게임종료
        print(second + 1)
        return

arr[0][0] = 1
dfs(arr, 0, (0, 0), 0, 1)
