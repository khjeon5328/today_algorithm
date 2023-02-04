import sys


sys.stdin = open('input.txt')


def brute(y, x, arr):
    cnt1 = 0
    cnt2 = 0
    for i in range(y, y+8):
        for j in range(x, x+8):
            if (i + j) % 2:
                if arr[i][j] != 'W': cnt1 += 1
                if arr[i][j] != 'B': cnt2 += 1
            else:
                if arr[i][j] != 'B': cnt1 += 1
                if arr[i][j] != 'W': cnt2 += 1
    
    return min(cnt1, cnt2)



N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
# print(arr)
minV = N*M
for y in range(N-8+1):
    for x in range(M-8+1):
        res = brute(y, x, arr)
        if res < minV:
            minV = res

print(minV)

