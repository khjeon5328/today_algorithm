import sys


sys.stdin = open('input.txt')


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

n = min(N, M)
ans = 1
for i in range(1, n):
    for y in range(N-i):
        for x in range(M-i):
            if arr[y][x] == arr[y+i][x+i] == arr[y+i][x] == arr[y][x+i]:
                ans = i + 1
                # print(arr[y][x], i)
print(ans**2)
        
