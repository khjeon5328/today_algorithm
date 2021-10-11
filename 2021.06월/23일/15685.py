import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

arr = [[0]*101 for _ in range(101)]

N = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    # print(x, y, d, g)
    arr[y][x] = 1
    ds = [d]
    tmp = [d]
    for _ in range(g + 1):
        for i in tmp:
            y += dy[i]
            x += dx[i]
            arr[y][x] = 1
        tmp = [(i+1)%4 for i in ds]   
        tmp.reverse()
        ds = ds + tmp
ans =0 
for y in range(100):
    for x in range(100):
        if arr[y][x] and arr[y+1][x] and arr[y][x+1] and arr[y+1][x+1]:
            ans += 1
print(ans)
