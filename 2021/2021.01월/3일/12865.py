import sys


sys.stdin = open('input.txt')

N, K = map(int, input().split())
arr = []
for _ in range(N):
    w, v = map(int, input().split())
    arr.append([w, v])
# print(arr)
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= arr[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1][0]] + arr[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]
# from pprint import pprint
print(dp[-1][-1])