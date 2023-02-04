import sys


sys.stdin = open('input.txt')

N = int(input())
arr = [[' ']*N for _ in range(N)]
for y in range(N-1, -1, -1):
    for x in range(N-1-y, N):
        arr[y][x] = '*'
for i in arr:
    print("".join(i))