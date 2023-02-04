import sys


sys.stdin = open('input.txt')

N = int(input())

arr = list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = arr[0]
# dp[2] = max(dp[1]*2, arr[1])

for i in range(2, N+1):
    dp[i] = arr[i-1]
    for j in range(1, i):
        dp[i] = max(dp[i], dp[i-j] + dp[j])
print(dp[-1])
