import sys


sys.stdin = open('input.txt')
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def cut(y, x, n):
    global white, blue

    for i in range(y, y + n):
        for j in range(x, x + n):
            if arr[i][j] != arr[y][x]:
                #1
                cut(y, x, n//2)
                #2
                cut(y, x+n//2, n//2)
                #3
                cut(y+ n//2, x, n//2)
                #4
                cut(y+n//2, x+ n//2, n//2)
                return
    if arr[y][x]:
        blue += 1
    else:
        white += 1  
cut(0, 0, N)
print(white)
print(blue)