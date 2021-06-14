import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
board = [[0] * 6 for _ in range(6)]

from collections import deque

path = deque()
for _ in range(36):
    tmp = list(input())
    x = tmp[0]
    x = ord(x) - 65
    y = int(tmp[1]) - 1 
    path.append((y, x))

start_y, start_x = path.popleft()
board[start_y][start_x] = 1
possible_y = []
possible_x = []
for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
    possible_y.append(start_y + dy)
    possible_x.append(start_x + dx)
flag = True
while path:
    y, x = path.popleft()
    if y in possible_y and x in possible_x and not board[y][x]:
        board[y][x] = 1
        possible_y = []
        possible_x = []
        for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
            possible_y.append(y + dy)
            possible_x.append(x + dx)
    else:
        flag = False
        break

if flag and start_y in possible_y and start_x in possible_x:
    print('Valid')
else:
    print('Invalid')
