import sys


sys.stdin = open('input.txt')


N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
# print(arr)
dp = [0] * (K+1)
dp[0] = 1
for i in arr:
    for j in range(1, K+1):
        if (j - i) >= 0:
            dp[j] += dp[j-i]
print(dp[K])