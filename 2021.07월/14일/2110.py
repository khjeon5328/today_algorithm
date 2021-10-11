import sys


sys.stdin = open('input.txt')

N, C = map(int, input().split())

houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()
low = 1
high = houses[-1] - houses[0]

def router(distance):
    cnt = 1
    tmp = houses[0]
    for i in range(1, N):
        if tmp + distance <= houses[i]:
            cnt += 1
            tmp = houses[i]
    return cnt

answer = 0
while low <= high:
    mid = (low + high) // 2

    cnt = 0
    if router(mid) >= C:
        low = mid + 1
    else:
        high = mid - 1

print(high)

