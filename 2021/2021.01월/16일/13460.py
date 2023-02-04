import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

from collections import deque

N, M = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(N)]
# print(arr)
visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

def init():
    _rx, _ry, _bx, _by = [0] * 4
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                _rx, _ry = i, j
            elif arr[i][j] == 'B':
                _bx, _by = i, j
    q.append((_rx, _ry, _bx, _by, 0))
    visited[_rx][_ry][_bx][_by] = True

def move(_x, _y, _dx, _dy, _c):
    while arr[_x + _dx][_y + _dy] != '#' and arr[_x][_y] != 'O':
        _y += _dy
        _x += _dx
        _c += 1
    return _x, _y, _c

def bfs():
    init()
    while len(q):
        rx, ry, bx, by, d = q.popleft()

        if d > 10:
            print(-1)
            return

        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            
            if arr[nrx][nry] == 'O':
                print(d + 1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx-dx[i], nry-dy[i]
                else:
                    nbx, nby = nbx-dx[i], nby-dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))

bfs()





    