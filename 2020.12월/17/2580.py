import sys


sys.stdin = open('input.txt')
from pprint import pprint

def horizontal(y, val):
    if val in arr[y]:
        return False
    return True

def vertical(x, val):
    for i in range(9):
        if val == arr[i][x]:
            return False
    return True

def byThree(y, x, val):
    shareY = y // 3
    shareX = x // 3
    for y in range(shareY*3, (shareY+1)*3):
        for x in range(shareX*3, (shareX+1)*3):
            if arr[y][x] == val:
                return False
    return True

flag = False
def dfs(k):
    global flag
    if flag:
        return

    if k == len(blank):
        for i in range(9):
            print(*arr[i])
        flag = True
        return
    
    for i in range(1, 10):
        ny, nx = blank[k][0], blank[k][1]
        if horizontal(ny, i) and vertical(nx, i) and byThree(ny, nx, i):
            arr[ny][nx] = i
            dfs(k+1)
            arr[ny][nx] = 0


arr = [list(map(int, input().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]
dfs(0)