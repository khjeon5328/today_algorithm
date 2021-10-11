import sys


sys.stdin = open('input.txt')

N, K = map(int, input().split())

lope = []
for _ in range(N):
    lope.append(int(input()))
v = max(lope)

low = 1
high = v

while low <= high:
    mid = (low + high) // 2

    cnt = 0
    for i in lope:
        cnt += (i // mid)

    if cnt < K:
        high = mid - 1
    elif cnt >= K:
        low = mid + 1
    
print(high)
    