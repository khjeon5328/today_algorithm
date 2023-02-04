import sys


sys.stdin = open('input.txt')

N = int(input())
K = int(input())

B = []
A = [[0]*N for _ in range(N)]
for y in range(1,N+1):
    for x in range(1, N+1):
        A[y-1][x-1] = y*x
        B.append(y*x)
from pprint import pprint
pprint(A)
B.sort()
print(B)
print(B[K-1])

low = 1
high = N * N
while low <= high:
    mid = (low + high) // 2

    cnt = 0
    for i in range(1, N+1):
        cnt += (mid // i)
    if cnt > K+1:
        high = mid - 1
    else:
        low = mid + 1
print(high)

